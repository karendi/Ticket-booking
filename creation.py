import os
import sys
from sqlalchemy import Column , ForeignKey , Integer , String , DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Event(Base):
    __tablename__ = 'Event'
    #define the columns for the event table
    Name = Column(String(250) , nullable = False )
    Month = Column(String(250))
    Venue = Column(String(250))
    Event_id = Column(Integer , nullable = False ,primary_key =True)



class Ticket(Base):
    __tablename__ ='Ticket'

    Ticket_No = Column(Integer , primary_key = True )
    Event = Column(Integer ,ForeignKey('Event.Event_id'))



#create an engine that stores data in the local directory's
engine = create_engine('sqlite:///ticket_booking.db')

#create all tables is the engine. same as Create Table in sql
Base.metadata.create_all(engine)
