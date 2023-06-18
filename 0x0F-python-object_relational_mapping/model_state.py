#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, ForeignKey  # create_engine
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    '''
    A python file that contains the class definition of a State and an\
            instance Base = declarative_base()
    '''
    __tablename__ = 'states'

    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column('name', String(128), nullable=False)


'''
    def __init__(self, name, id=0):
        self.id = id
        self.name = name
'''
'''
engine = create_engine('mysql://username=root@localhost:3306/\
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
'''
