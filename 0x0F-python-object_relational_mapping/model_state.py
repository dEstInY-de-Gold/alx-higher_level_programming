#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlachemy.orm import sessionMaker

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String, CHAR)

    def __init__(self, id, name):
        self.id = id
        self.name = name

engine = create_engine('mysql://username=password@localhost:3306/
                        hbtn_0e_6_usa')

# Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

# Usage example: adding a new state to the table
    new_state = State(name='California')
    session.add(new_state)
    session.commit()

# Close the session when done
    session.close()
