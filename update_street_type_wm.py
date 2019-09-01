#!/usr/bin/env python
# coding: utf-8

# In[ ]:


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons", "Circle", "Highway", "Terrace", "Pike", "West", "Way", 
            "North", "East", "South", "A", "58", "School", "Loop"]

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            "st." : "Street",
            "st" : "Street",
            "Ave": "Avenue",
            "Ave." : "Avenue",
            "ave" : "Avenue",
            "ave." : "Avenue",
            "Blvd" : "Boulevard",
            "Rd": "Road",
            "Rd.": "Road",
            "road" : "Road",
            "Cir" : "Circle",
            "Ct" : "Court",
            "Dr" : "Drive",
            "Dr." : "Drive",
            "dr." : "Drive",
            "Hwy" : "Highway",
            "Ln" : "Lane",
            "N" : "North",
            "drive" : "Drive"

            }

def update_street_type(name):
    for old_type in mapping:
        if name.endswith(old_type):
            new_type = mapping[old_type]
            name = name[:(len(name) - len(old_type))] + new_type
    return name

