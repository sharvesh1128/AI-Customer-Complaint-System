from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:111212@localhost:5432/complaint_db"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        print("Database Connected Successfully!")
except Exception as e:
    print("Connection Failed")
    print(e)