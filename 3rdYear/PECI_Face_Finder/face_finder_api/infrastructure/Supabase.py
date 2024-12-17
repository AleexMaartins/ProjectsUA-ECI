from dotenv import load_dotenv
from supabase import create_client
import os

load_dotenv()

class Supabase:
    def __init__(self):
        self.supabase = create_client(os.getenv("SB_URL"), os.getenv("SB_KEY"))