# lib/cli.py
from tabulate import tabulate
from lib.db.models import Reservation, session, Customer, Table
from datetime import datetime

def create_reservation():
    customer_id = int(input("Customer ID: "))
    table_id = int(input("Table ID: "))
    date_str = input("Date (YYYY-MM-DD): ")
    time_str = input("Time (HH:MM): ")

    try:
        reservation_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        reservation_time = datetime.strptime(time_str, "%H:%M").time()

        customer = session.query(Customer).get(customer_id)
        table = session.query(Table).get(table_id)

        if not customer:
            print("Customer not found.")
            return
        if not table:
            print("Table not found.")
            return

        reservation = Reservation(
            customer=customer,
            table=table,
            reservation_date=reservation_date,
            reservation_time=reservation_time
        )
        session.add(reservation)
        session.commit()
        print("Reservation created.")
    except Exception as e:
        print("Error creating reservation:", e)

def view_reservations_by_date():
    date_str = input("Enter date to view reservations (YYYY-MM-DD): ").strip()
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
        reservations = session.query(Reservation).filter_by(reservation_date=date_obj).all()

        if reservations:
            table_data = []
            for r in reservations:
                customer_name = r.customer.name if r.customer else "Unknown"
                table_number = r.table.table_number if r.table else "Unknown"
                res_time = r.reservation_time.strftime("%H:%M")
                table_data.append([r.id, customer_name, table_number, res_time])
            
            print("\nReservations:")
            print(tabulate(table_data, headers=["ID", "Customer", "Table", "Time"], tablefmt="grid"))
        else:
            print("No reservations for that date.")
    except Exception as e:
        print("Invalid date or error:", e)

def add_customer():
    name = input("Customer name: ")
    phone = input("Contact: ")
    customer = Customer(name=name, phone=phone)
    session.add(customer)
    session.commit()
    print("Customer added.")

    # Optional: list customers
    customers = session.query(Customer).all()
    table_data = [[c.id, c.name, c.phone] for c in customers]
    print("\nAll Customers:")
    print(tabulate(table_data, headers=["ID", "Name", "Contact"], tablefmt="grid"))

def main():
    while True:
        print("\n--- Restaurant Reservation System ---")
        print("1. Add Customer")
        print("2. Create Reservation")
        print("3. View Reservations by Date")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_customer()
        elif choice == '2':
            create_reservation()
        elif choice == '3':
            view_reservations_by_date()
        elif choice == '4':
            print("Mambo iko top!")
            break
        else:
            print("Invalid choice. Try again.")
