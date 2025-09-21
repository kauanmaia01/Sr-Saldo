from supabase import create_client
from dotenv import load_dotenv
import os


load_dotenv()

class DbCreateClient:
    def __init__(self):
        self.database_url = os.getenv('SUPABASE_URL')
        self.database_key = os.getenv('SUPABASE_KEY')

    
    def create_session(self):
        client = create_client(supabase_url=self.database_url, supabase_key=self.database_key)
        return client
    

    def database_interaction(self, database_nm: str):
        response = self.create_session()
        return response.table(database_nm)
