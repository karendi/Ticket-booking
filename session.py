import smtplib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from creation import Event , Ticket

engine = create_engine('sqlite:///ticket_booking.db')
Base = declarative_base()
Base.metadata.bind = engine


Session = sessionmaker(bind=engine)

session = Session()

#deleting an event
def delete_event(event_id):
    query = session.query(Event).filter_by(Event_id = event_id)
    if query.count() == 0:
        return"The event doesn't exist"

    else:
        query.delete()
        session.commit()
        return "The event with the id , " +  event_id + "has been deleted"





def edit_event(event_name , month , venue , event_id):
    edit_event = session.query(Event).filter(Event.Event_id == event_id).first()
    edit_event.Name = event_name
    edit_event.Month = month
    edit_event.Venue = venue
    session.commit()
    return "The event:" + event_name + "has been updated"





def send_ticket(email , ticket_no):
    query = session.query(Ticket).filter(Ticket.Ticket_No == ticket_no).all()
    for row in query:
        ticket_number = str(row.Ticket_No)
        event = (row.Event)
        message = "\nThis is your ticket for the event with id: {0}.The ticket number is {1}".format(event, ticket_number)

        #import pdb; pdb.set_trace()
        server = smtplib.SMTP('smtp.gmail.com' ,587) #create an smtp object
        server.ehlo()
        server.starttls()
        server.login("electionpollskenya@gmail.com" ,"ngurorachel") #log in to server
        #send the mail
        server.sendmail("electionpollskenya@gmail.com" , email , message)
        server.close()
