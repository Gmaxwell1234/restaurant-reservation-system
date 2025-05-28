# lib/debug.py
from lib.db.models import engine
from sqlalchemy import inspect

inspector = inspect(engine)
tables = inspector.get_table_names()
print("Tables in database:", tables)

for table in tables:
    print(f"\nColumns in {table}:")
    for column in inspector.get_columns(table):
        print(f"{column['name']} ({column['type']})")
