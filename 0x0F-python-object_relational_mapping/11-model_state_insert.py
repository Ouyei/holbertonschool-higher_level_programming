#!/usr/bin/python3
"""
Adds the State object “Louisiana” to
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

    # Add new record
    lou_state = State(name='Louisiana')
    session.add(lou_state)
    session.commit()

    # Print query
    print('{0}'.format(lou_state.id))

    # Close session
    session.close()
