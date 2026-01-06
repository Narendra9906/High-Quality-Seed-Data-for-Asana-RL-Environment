import sqlite3
import logging
from config import DB_PATH, SCHEMA_PATH

logger = logging.getLogger(__name__)

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row  # Access columns by name
        return conn
    except sqlite3.Error as e:
        logger.error(f"Database connection failed: {e}")
        raise

def setup_database():
    """Initializes the database using schema.sql."""
    logger.info(f"Setting up database at {DB_PATH}...")
    
    # Ensure directory exists
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        with open(SCHEMA_PATH, 'r') as f:
            schema_script = f.read()
        
        # execute_script executes multiple SQL statements
        cursor.executescript(schema_script)
        conn.commit()
        logger.info("Database schema applied and seed data inserted successfully.")
    except Exception as e:
        logger.error(f"Failed to setup database: {e}")
        conn.rollback()
        raise
    finally:
        conn.close()