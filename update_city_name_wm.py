#!/usr/bin/env python
# coding: utf-8

# In[ ]:


expected = ['Chattanooga','East Ridge','Harrison','Lookout Mountain','Ooltewah','Red Bank']

# UPDATE THIS VARIABLE
mapping = { "Brainiard": "Brainerd",
            "brainerd": "Brainerd",
            "Ch" : "Chattanooga",
            "Chatanooga" : "Chattanooga",
            "Chattanooga, TN": "Chattanooga",
            "Chattanoooga" : "Chattanooga",
            "Chattaoooga" : "Chattanooga",
            "chattanooga" : "Chattanooga",
            "east Ridge" : "East Ridge",
            "hixson": "Hixson",
            "ooltewah": "Ooltewah",
            "red bank" : "Red Bank",
            "redbank" : "Red Bank",
            "Red bank" : "Red Bank",
            }

def update_city_name(name):
    if name not in expected:
        for old_name in mapping:
            if name == old_name:
                name = mapping[old_name]
    return name

