from models.event import *


event_01 = Event("4/15/2021", "salsa_party", 50, "salsa_room", "Introductory Class followed by social dancing")
event_02 = Event("4/16/2021", "bachata_party", 50, "bachata_room", "Introductory Class followed by social dancing")
event_03 = Event("4/17/2021", "kizomba_party", 50, "kizomba_room", "Introductory Class followed by social dancing")
event_04 = Event("4/18/2021", "forro_party", 50, "forro_room", "Introductory Class followed by social dancing")

all_events =[event_01, event_02, event_03, event_04]





def add_new_event(event):
    all_events.append(event)
    
    occurrance=0
    for each_event in all_events:
        if each_event.name == event.name:
            occurrance += 1
    i= 0
    print (occurrance)
    while i <len(all_events):
            # for each_event in all_events:
            # print(each_event)
            if all_events[i].name == event.name and occurrance > 1:
                all_events[i].recurring = True
            i += 1




# def set_recurring(event):
#     event.recurring = True

def remove_selected_event(event_name, date):

    i=0
    while(i<len (all_events)):
        print(all_events[i].name)
        print(event_name)
        
        if all_events[i].name == event_name :
            if  all_events[i].recurring == True and recurring_count(event_name)== 2 :
                set_recurring_false(event_name)
                all_events.remove( all_events[i])
            
            else:
                all_events.remove( all_events[i])
        i += 1


def recurring_count(event_name):
    count = 0
    for each_event in all_events:
        if each_event.name == event_name:
            count += 1
    return count

def set_recurring_false(event_name):
        i= 0
        while i <len(all_events):

            if all_events[i].name == event_name:
                all_events[i].recurring = False
            i += 1

