#!/usr/bin/python3

from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta

class Event:
    start_date = datetime.now()
    end_date = datetime.now()
    event_name = None

    def __init__(self, name = "Untitled event", start_date = datetime.today(),
                end_date = None):
        self.start_date = start_date
        if (end_date == None):
            end_date = start_date + timedelta(hours = 1)
        self.end_date = end_date
        self.event_name = name

    def change_name(self, name = "Untitled event"):
        print("Setting event: {}'s name to {}".format(self.event_name, name))
        self.event_name = name

    def change_date(self, day=start_date.day, month=start_date.month,
                   year=start_date.year, mode = ""):
        if mode == "s":
            print("Setting event: {}'s start date to {}/{}/{}".format(
                self.event_name, month, day, year))
            self.start_date = datetime(year = year, day = day, month = month, hour
                                  = self.start_date.hour, minute =
                                   self.start_date.minute)
        elif mode == "e":
            print("Setting event: {}'s end date to {}/{}/{}".format(
                self.event_name, month, day, year))
            self.end_date = datetime(year = year, day = day, month = month, hour
                                  = self.end_date.hour, minute =
                                   self.end_date.minute)

    def change_time(self, hour=start_date.hour, minute=start_date.minute, mode = ""):
        if mode == "s":
            print("Setting event: {}'s start time to {}:{}".format(
                self.event_name, hour, minute))
            self.start_date = datetime(year = self.start_date.year, day =
                                       self.start_date.day, month =
                                       self.start_date.month, hour
                                       = hour, minute = minute)
        elif mode == "e":
            print("Setting event: {}'s start time to {}:{}".format(
                self.event_name, hour, minute))
            self.end_date = datetime(year = self.end_date.year, day =
                                       self.end_date.day, month =
                                       self.end_date.month, hour
                                       = hour, minute = minute)

class Task:
    task_name = datetime.now()
    deadline = datetime.now()
    priority = 0

    def __init__(self, name = "Untitled task", deadline = datetime.today(),
                 priority = 0):
        self.task_name = name
        self.deadline = deadline
        self.priority = priority

    def change_name(self, name = "Untitled task"):
        print("Setting task: {}'s name to {}".format(self.task_name, name))
        self.task_name = name

    def change_date(self, day = deadline.day, month = deadline.month,
                    year = deadline.year):
        print("Setting task: {}'s deadline to {}/{}/{}".format(self.task_name,
                                                               month, day,
                                                               year))
        self.deadline = datetime(year = year, day = day, month = month, hour
                                  = self.deadline.hour, minute =
                                   self.deadline.minute)

    def change_time(self, hour=deadline.hour, minute=deadline.minute):
        print("Setting task: {}'s due time to {}:{}".format(
             self.task_name, hour, minute))
        self.deadline = datetime(year = self.deadline.year, day =
                                       self.deadline.day, month =
                                       self.deadline.month, hour
                                       = hour, minute = minute)

    def change_priority(self, priority):
        print("Setting task: {}'s priority to {}".format(self.task_name,
                                                         priority))
        self.priority = priority

def load_event(data):
    events = []
    for line in data:
        if line[0:1] == "T":
            continue
        if line == "":
            continue
        else:
            year, month, day, hour, minute, e_year, e_month, e_day, e_hour, e_minute, name = line.split("#")
            start = datetime(year = int(year), month = int(month),
                         day = int(day), hour = int(hour), minute = int(minute))
            end = datetime(year = int(e_year), month = int(e_month),
                       day = int(e_day), hour = int(e_hour), minute =
                       int(e_minute))
            name = name[:-1]
            events.append(Event(name, start, end))
    return events

def load_tasks(data):
    tasks = []
    for line in data:
        if line[0:1] == "T":
            line = line[1:]
            year, month, day, hour, minute, priority, name = line.split("#")
            deadline = datetime(year = int(year), month = int(month),
                         day = int(day), hour = int(hour), minute = int(minute))
            prio = int(priority)
            name = name[:-1]
            tasks.append(Task(name, deadline, prio))
    return tasks

def main():
    events = []
    tasks = []
    file_name = input("Enter the name of the workbook you wish to use:\n")
    ref_file = open(file_name, 'r')
    data = ref_file.readlines()
    events = load_event(data)
    tasks = load_tasks(data)

    command = input("Welcome to DoingIt! Please enter a command. Type menu to see options:\n")
    while command != 'quit':

        if (command == 'menu'):
            print("""Menu options:
file       = Choose a taskbook to work in
addevent   = Create an event
addtask    = Create a task
updateevent= Update an event
updatetask = Update a task
deleteevent= Delete an event
deletetask = Delete a task
showevents = Show events
showtasks  = Show tasks in priority order
quit       = Quit the program""")

        if (command == 'file'):
            file_name = input("Enter the name of the workbook you wish to use:\n")
            ref_file.close()
            ref_file = open(file_name, 'r')
            data = ref_file.readlines()
            events = load_event(data)
            tasks = load_tasks(data)

        if (command == 'addevent'):
            name = input("Please input the name of the event: \n")
            line = input("""Please input the start date of the event in the
format MM/DD/YYYY:\n""")
            month, day, year = line.split("/")
            line = input("""Please input the start time of the event in the
format HH:MM:\n""")
            hour, minute = line.split(":")
            events.append(Event(name, datetime(year = int(year), month =
                                                   int(month), day = int(day),
                                                   hour = int(hour),
                                                   minute = int(minute))))

        if (command == 'addtask'):
            name = input("Task name: \n")
            line = input("Task deadline in the format MM/DD/YYYY:\n")
            month, day, year = line.split("/")
            line = input("Task deadline time in the format HH:MM\n")
            hour, minute = line.split(":")
            priority = int(input("Task priority (1-4)\n"))
            deadline = datetime(year = int(year), month = int(month), day =
                                int(day), hour = int(hour), minute =
                                int(minute))
            tasks.append(Task(name, deadline, priority))

        if (command == 'updateevent'):
            name = input("Which event would you like to update?\n")
            for i in events:
                if i.event_name == name:
                    change = input("""c = Change the name
s = Change the start date
e = Change the end date
st = Change the start time
et = Change the end time\n""")
                    if change == "c":
                        name = input("Enter the new event name:")
                        i.change_name(name)
                    if change == "s":
                        line = input("""Please input the start date of the event in the
format MM/DD/YYYY:\n""")
                        month, day, year = line.split("/")
                        i.change_date(int(day), int(month), int(year), change)
                    if change == "e":
                        line = input("""Please input the end date of the event in the
format MM/DD/YYYY:\n""")
                        month, day, year = line.split("/")
                        i.change_date(int(day), int(month), int(year), change)
                    if change == "st":
                        line = input("""Please input the start time of the event in the
format HH:MM:\n""")
                        hour, minute = line.split(":")
                        i.change_time(int(hour), int(minute), change[0:1])
                    if change == "et":
                        line = input("""Please input the end time of the event in the
format HH:MM:\n""")
                        hour, minute = line.split(":")
                        i.change_time(int(hour), int(minute), change[0:1])

        if (command == 'updatetask'):
            name = input("Task to update:\n")
            for i in tasks:
                if i.task_name == name:
                    change = input("""c = Change the name
s = Change the deadline
t = Change the due time
p = Change the priority\n""")
                    if change == "c":
                        name = input("New task name:")
                        i.change_name(name)
                    if change == "s":
                        line = input("""New deadline for the task in the
format MM/DD/YYYY:\n""")
                        month, day, year = line.split("/")
                        i.change_date(int(day), int(month), int(year))
                    if change == "t":
                        line = input("""New due time for the task in the
format HH:MM:\n""")
                        hour, minute = line.split(":")
                        i.change_time(int(hour), int(minute))
                    if change == "p":
                        prio = input("New priority for the task (1-4)\n")
                        i.change_priority(int(prio))

        if (command == 'deleteevent'):
            name = input("Input the name of the event you would like to delete:\n")
            for i in events:
                if i.event_name == name:
                    events.remove(i)

        if (command == 'deletetask'):
            name = input("Task to delete:\n")
            for i in tasks:
                if i.task_name == name:
                    tasks.remove(i)

        if (command == 'showevents'):
            for i in events:
                print(i.event_name + ":")
                print(i.start_date.strftime("Start time: %I:%M %p"))
                print(i.start_date.strftime("Start day: %a, %b %d, %y") + "\n")
                print(i.end_date.strftime("End time: %I:%M %p"))
                print(i.end_date.strftime("End day: %a, %b %d, %y") + "\n")

        if (command == 'showtasks'):
            for i in tasks:
                print(i.task_name + ":")
                print(i.deadline.strftime("Due at: %I:%M %p on %a, %b %d, %y"))
                print("Priority: {}".format(i.priority))

        command = input("Please input your next command:\n")

    ref_file.close()
    ref_file = open(file_name, 'w')
    for i in events:
        ref_file.write(i.start_date.strftime("%Y#%m#%d#%H#%M#") +
                       i.end_date.strftime("%Y#%m#%d#%H#%M#") + i.event_name +
                      "\n")
    for i in tasks:
        ref_file.write("T" + i.deadline.strftime("%Y#%m#%d#%H#%M#") +
                       str(i.priority) + "#" + i.task_name + "\n")
    ref_file.close()

    print("Goodbye!")


if __name__ == "__main__":
    main();
