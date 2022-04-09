#!/usr/bin/python3
"""
Deletes all State objects with a name containing the
letter 'a' from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Deletes State objects on the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Initialize engine
    engine = create_engine(db_uri)

    # Initialize session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Update record
    for instance in session.query(State).filter(State.name.contains('a')):
        session.delete(instance)

    session.commit()

    # Close session
    session.close()
