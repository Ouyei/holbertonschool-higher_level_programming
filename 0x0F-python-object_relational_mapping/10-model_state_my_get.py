#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from
the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Initialize engine
    engine = create_engine(db_uri)

    # Initialize session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    instance = session.query(State).filter(State.name == argv[4]).first()

    # Conditions
    if instance is None:
        print('Not found')
    else:
        print('{0}'.format(instance.id))

    # Close session
    session.close()
