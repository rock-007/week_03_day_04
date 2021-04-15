from models.event import *


event_01 = Event("4/15/2021", "salsa_party", 50, "salsa_room", "Introductory Class followed by social dancing")
event_02 = Event("4/16/2021", "bachata_party", 50, "bachata_room", "Introductory Class followed by social dancing")
event_03 = Event("4/17/2021", "kizomba_party", 50, "kizomba_room", "Introductory Class followed by social dancing")
event_04 = Event("4/18/2021", "forro_party", 50, "forro_room", "Introductory Class followed by social dancing")

all_events =[event_01, event_02, event_03, event_04]





def add_new_event(event):
    if event.name in all_events:
        all_events.append(event)
        i=0
        while i <len(all_events):
            # for each_event in all_events:
            # print(each_event)
            if all_events[i].name == event.name:
                all_events[i].recurring = True
            i += 1

                

    else:
        print( len (all_events))
        all_events.append(event)



# def set_recurring(event):
#     event.recurring = True


