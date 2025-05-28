# Restaurant Reservation System

A command-line application to manage restaurant customers, tables, and reservations using Python, SQLAlchemy ORM, and SQLite.

##  Features

- Add new customers to the system.
- Create table reservations.
- View all reservations for a specific date in a neat table format.
- Enforces table capacity and prevents overlapping reservations.

##  Tech Stack

- **Language:** Python 3
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Testing:** unittest
- **Development Environment:** pipenv

##  Project Structure
restaurant-reservation-system/
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib/
├── cli.py # Main interactive CLI logic
├── debug.py # Script to debug or inspect database
├── helpers.py # Utility/helper functions
└── db/
├── models.py # SQLAlchemy ORM models
├── seed.py # Script to seed database with dummy data
├── config.py # Database configuration
└── migrations/ # Alembic migration files (optional)

##  Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/restaurant-reservation-system.git
   cd restaurant-reservation-system
2. Install dependencies
    pipenv install
3. Activate pipenv shell
    pipenv shell
4. Run seed script
    pipenv run python lib/db/seed.py
5. Run the program
    pipenv run python main.py
# Usage
-Follow the menu options to:

-Add customers

-Make reservations

-View reservations by date

# Running Tests
-If you've written unit tests:
-python -m unittest discover tests
# Author
Maxwell Githinji
muriumaxwell1@gmail.com


