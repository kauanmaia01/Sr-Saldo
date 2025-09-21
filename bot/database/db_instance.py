from sqlalchemy import create_engine, insert, delete, text
from sqlalchemy.engine import URL
import pandas as pd
import dotenv, os

dotenv.load_dotenv()

url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres.hfmoxzfwhvkqotcefwiz",
    password=os.getenv("DB_PASSWORD"),
    host="aws-0-sa-east-1.pooler.supabase.com",
    port=5432,
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


    def get_data(self, query: str) -> pd.DataFrame:
        result = self._db_connection(text(query))
        return pd.DataFrame(result.mappings().all())


    def insert_data(self, table_obj, id_name: str, assets_type: str, assets_name: str, 
                    current_quote: float, amount: int, buy_date: str) -> int:
        stmt = (
            insert(table_obj)
            .values(
                assets_type=assets_type,
                assets_name=assets_name,
                current_quote=current_quote,
                amount=amount,
                buy_date=buy_date
            )
            .returning(table_obj.c[id_name])
        )
        return self._db_connection(stmt, operation_type=1).scalar()


    def delete_data(self, table_obj, column, value) -> None:
        stmt = delete(table_obj).where(column == value)
        self._db_connection(stmt, operation_type=1)



#db_action = DbInstance()


#data = "Ação", "PETR4", "34.99", 5, "2025-07-20"

# Select Insert data

# test = DbInstance()
# insert_data = test.insert_data(table_obj=tb_assets, id_name='assets_id', assets_type="Ação", assets_name="PETR3", current_quote="34.99", amount=5, buy_date="2025-07-20")
# print(insert_data)

# Select data

#test = DbInstance()
#df_assets = test.get_data("SELECT * FROM tb_assets;")
#print(df_assets)

# Delete data

#test = DbInstance()
#assets = test.delete_data(tb_assets, "assets_id = 3")