import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager:
    def __init__(self):
        self.engine = self._create_engine()

    def _create_engine(self):
        try:
            url = (
                f"postgresql+psycopg2://{os.getenv('DB_USER')}:"
                f"{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:"
                f"{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
            )
            return create_engine(url)
        except Exception as e:
            print(f"Connection error: {e}")
            raise

    def read_table(self, table: str, columns: list[str]) -> pd.DataFrame:
        query = f"SELECT {', '.join(columns)} FROM {table};"
        try:
            return pd.read_sql(query, self.engine)
        except Exception as e:
            print(f"Error reading data: {e}")
            return pd.DataFrame()