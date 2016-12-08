import sqlite3

connection = sqlite3.connect("ticket_booking.db")
cursor = connection.cursor()


class ManipulateEvent(object):
    def __init__(self, name, month, venue , event_id):
        self.name = name
        self.month = month
        self.venue = venue
        self.event_id = event_id

    def save_event(self):
        add_event = '''
		INSERT INTO Event (Name, Month , Venue , Event_id)
		VALUES ('{0}', '{1}' ,'{2}' ,'{3}')
		'''.format(self.name, self.month, self.venue , self.event_id)

        if cursor.execute(add_event):
            connection.commit()
            return "Your event has been added!"
        return "Error while adding the event!"

    def list_events(self):
        get_all_events_query = '''
        SELECT * FROM Event
        '''
        if cursor.execute(get_all_events_query):
            events = cursor.fetchall()
            return events

class ManipulateTicket(object):
    def __init__(self , ticket_no , event_id ):
        self.ticket_no = ticket_no
        self.event_id = event_id


    def generate_ticket(self):
        add_ticket = '''
		INSERT INTO Ticket (Ticket_No, Event )
		VALUES ('{0}', '{1}' )
		'''.format(self.ticket_no, self.event_id)

        if cursor.execute(add_ticket):
            connection.commit()
            return "Your ticket for has been generated!"
        return "Error generating your ticket!"

    def list_tickets(self):
        get_all_tickets_query = '''
        SELECT * FROM Ticket
        '''
        if cursor.execute(get_all_tickets_query):
            tickets = cursor.fetchall()
            return tickets
