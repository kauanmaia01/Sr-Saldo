from sqlalchemy import create_engine, insert, delete, text
from sqlalchemy.engine import URL
import dotenv, os
import urllib.parse

dotenv.load_dotenv()

password = urllib.parse.quote_plus(os.getenv("DB_PASSWORD", ""))

url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=password,
    host="aws-1-us-west-2.pooler.supabase.com",
    port=6543,
    database="postgres"
)

class DbInstance:
    def __init__(self):
        self._engine = create_engine(url, echo=os.getenv("DEBUG", False))


    def _db_connection(self, stmt, operation_type: int = 0):
        """operation_type=0: SELECT | 1: INSERT/DELETE/UPDATE"""
        with self._engine.connect() as conn:
            result = conn.execute(stmt)
            if operation_type == 0:
                return result
            conn.commit()
            return result


    def insert_data(self, table_obj, values: dict, id_name: str = None) -> int | None:
        stmt = insert(table_obj).values(**values)

        if id_name:
            stmt = stmt.returning(table_obj.c[id_name])

        result = self._db_connection(stmt, operation_type=1)
        return result.scalar() if id_name else None


    def delete_data(self, table_obj, column, value) -> None:
        stmt = delete(table_obj).where(getattr(table_obj.c, column) == value)
        self._db_connection(stmt, operation_type=1)