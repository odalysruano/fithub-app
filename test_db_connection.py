import os
import django
from django.conf import settings
from django.db import connections
from django.db.utils import OperationalError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fithub.settings')
django.setup()

def check_database_connection():
    db_conn = connections['default']
    try:
        c = db_conn.cursor()
        c.execute("SELECT 1;")
        print("Database connection successful.")
    except OperationalError as e:
        print(f"Database connection failed: {e}")
        raise e

if __name__ == "__main__":
    check_database_connection()
