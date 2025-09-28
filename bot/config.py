import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("TOKEN_BOT")
USER_ID = int(os.getenv("USER_ID"))