#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the cities
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
    query = session.query(City, State).join(State)

    # Print query --> s : state. c: city
    for _c, _s in query.all():
        print("{}: ({:d}) {}".format(_s.name, _c.id, _c.name))

    session.commit()

    # Close session
    session.close()
