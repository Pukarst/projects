import calendar
import datetime

def display_calendar(year, month):
    print(calendar.month(year, month))

def add_event(events, date, event):
    events[date] = event
    print(f"Event added: {event} on {date}")

def show_events(events, date):
    if date in events:
        print(f"Events on {date}: {events[date]}")
    else:
        print(f"No events on {date}")

def calendar_app():
    events = {}
    while True:
        print("\n1. Display Calendar\n2. Add Event\n3. Show Event\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            year = int(input("Enter year: "))
            month = int(input("Enter month: "))
            display_calendar(year, month)
        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD): ")
            event = input("Enter event: ")
            add_event(events, date, event)
        elif choice == '3':
            date = input("Enter date (YYYY-MM-DD): ")
            show_events(events, date)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

calendar_app()
