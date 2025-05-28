# lib/db/seed.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from faker import Faker
from lib.db.models import session, Customer, Table

fake = Faker()

def seed_data():
    print("Seeding data...")

    # Optional: Clear old data
    session.query(Customer).delete()
    session.query(Table).delete()
    session.commit()

    # Seed Customers
    for _ in range(3):
        customer = Customer(name=fake.name(), phone=fake.phone_number())
        session.add(customer)

    # Seed Tables
    for i in range(1, 4):
        table = Table(table_number=i, capacity=fake.random_int(min=2, max=6))
        session.add(table)

    session.commit()
    print("Seeding complete.")

    # Debug: show seeded data
    print("Customers:", session.query(Customer).all())
    print("Tables:", session.query(Table).all())

if __name__ == "__main__":
    seed_data()
