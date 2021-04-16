from models.event import *
from datetime import datetime

#datetime.strptime("14 Apr 21", "%d %b %y")
event_01 = Event("2021-04-12 00:00:00", "salsa_party", 50, "salsa_room", "Introductory Class followed by social dancing-salsa_party")
event_02 = Event("2021-04-13 00:00:00", "bachata_party", 52, "bachata_room", "Introductory Class followed by social dancing-bachata_party")
event_03 = Event("2021-04-14 00:00:00", "kizomba_party", 53, "kizomba_room", "Introductory Class followed by social dancing-kizomba_party")
event_04 = Event("2021-04-15 00:00:00", "forro_party", 51, "forro_room", "Introductory Class followed by social dancing-forro_party")

all_events =[event_01, event_02, event_03, event_04]





def add_new_event(event):
    all_events.append(event)
    occurrance = recurring_count(event.name)
    set_recurring_true(event.name, occurrance)
    
def recurring_count(event_name):
    count = 0
    for each_event in all_events:
        if each_event.name == event_name:
            count += 1
    return count

def set_recurring_true(event_name, occurrance):
        i= 0
        while i <len(all_events):
            if all_events[i].name == event_name and occurrance > 1:
                all_events[i].recurring = True
            i += 1






def remove_selected_event(event_name, date):



    
    i=0
    while(i<len (all_events)):




        
        if all_events[i].name == event_name and all_events[i].date == date :
            if  all_events[i].recurring == True and recurring_count(event_name)== 2  :
                set_recurring_false(event_name)
                all_events.remove( all_events[i])
            
            else:
                all_events.remove( all_events[i])
        i += 1





def set_recurring_false(event_name):
        i= 0
        while i <len(all_events):

            if all_events[i].name == event_name:
                all_events[i].recurring = False
            i += 1

