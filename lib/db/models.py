import os
import sys
from sqlalchemy import create_engine, Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Ensure root directory is in sys.path so we can import from lib.db.config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from lib.db.config import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    reservations = relationship("Reservation", back_populates="customer")

    def __repr__(self):
        return f"<Customer(id={self.id}, name={self.name})>"

class Table(Base):
    __tablename__ = 'tables'
    id = Column(Integer, primary_key=True)
    table_number = Column(Integer, unique=True)
    capacity = Column(Integer)
    reservations = relationship("Reservation", back_populates="table")

    def __repr__(self):
        return f"<Table(id={self.id}, number={self.table_number}, cap={self.capacity})>"

class Reservation(Base):
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    table_id = Column(Integer, ForeignKey('tables.id'))
    reservation_date = Column(Date)
    reservation_time = Column(Time)

    customer = relationship("Customer", back_populates="reservations")
    table = relationship("Table", back_populates="reservations")

    def __repr__(self):
        return f"<Reservation(id={self.id}, customer_id={self.customer_id}, table_id={self.table_id}, date={self.reservation_date})>"

# ✅ Ensure tables are created
Base.metadata.create_all(engine)
