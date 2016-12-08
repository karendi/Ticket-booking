"""
Usage:
    interface.py create_event <event_name> <month> <venue> <event_id>
    interface.py delete_event <event_id>
    interface.py event_edit <event_name> <month> <venue> <event_id>
    interface.py event_list
    interface.py quit
    interface.py ticket_generate <ticket_no> <event_id>
    interface.py send_ticket <email_address> <ticket_no>
    interface.py ticket_list

Arguments:
    <event_id> The event id
    <event_name> The name of the event
    <month> The month the event is happening
    <venue> The venue of the event
    <ticket_no>The ticket number for a particular event
    <email_address> The email address that the ticket should be sent
Options:
    -h , --help , Show this screen and exit

"""

from docopt import docopt, DocoptExit
import cmd
from event_functions import ManipulateEvent , ManipulateTicket
import session
from pyfiglet import Figlet


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def definition():
    print("#" * 160)
    print(Figlet(font = 'bulbhead').renderText('EVENT BOOKING SERVICES'))
    print("#" * 160)
    print("This program is supposed to help users create and manage their events")
    print("and also help in the generation of tickets")
    print(__doc__)


#thi class contains all the commands we need
class Event(cmd.Cmd):
    prompt = '<ticket booking>'

    @docopt_cmd
    def do_event_list(self, arg):
        """Usage: event_list """
        Event = ManipulateEvent.list_events(self)
        print("\t")
        print("\t Event Name".ljust(20) + "Month".ljust(15) + "Venue".ljust(15) +"Event_id".ljust(15))
        print("\t")
        for a in Event:
            print("\t" + a[0].ljust(15) + a[1].ljust(15) + a[2].ljust(15) +str(a[3]).ljust(15))


    # this method is responsible for creating a new event
    @docopt_cmd
    def do_create_event(self, arg):
        """Usage: create_event <event_name> <month> <venue> <event_id>"""

        Accepted_months = ["January" , "February" , "March" ,
         "April" ,"May" , "June" ,"July" , "August" ,"September" ,
          "October" ,"November","December"]
        name = arg['<event_name>']
        month = arg['<month>']
        venue = arg['<venue>']
        event_id = arg['<event_id>']
        #validating user input for months
        if month not in Accepted_months:
            print("Sorry you have to enter a valid month")
        else:
            new_event = ManipulateEvent(name, month, venue ,event_id)
            print(new_event.save_event())




    @docopt_cmd
    def do_delete_event(self , arg):
        """Usage: delete_event <event_id>"""
        name = arg['<event_id>']
        print(session.delete_event(name))

    @docopt_cmd
    def do_event_edit(self, arg):
        """Usage: event_edit  <event_name> <month> <venue> <event_id>"""
        name = arg['<event_name>']
        month = arg['<month>']
        venue = arg['<venue>']
        event_id = arg['<event_id>']
        print(session.edit_event(name , month , venue , event_id))

    @docopt_cmd
    def do_ticket_generate(self , arg):
        """Usage: ticket_generate <ticket_no> <event_id>"""
        ticket_no = arg['<ticket_no>']
        event_id =arg['<event_id>']

        new_ticket = ManipulateTicket(ticket_no, event_id )
        print(new_ticket.generate_ticket())

    @docopt_cmd
    def do_send_ticket(self , arg):
        """Usage: send_ticket <email_address> <ticket_no>"""
        email = arg['<email_address>']
        ticket_no = arg['<ticket_no>']
        session.send_ticket(email , ticket_no)

    @docopt_cmd
    def do_ticket_list(self , arg):
        """Usage: ticket_list"""
        print(ManipulateTicket.list_tickets(self))



    @docopt_cmd
    def do_quit(self, arg):
        """Usage: quit"""
        exit()



if __name__ == "__main__":
    definition()
    Event().cmdloop()
