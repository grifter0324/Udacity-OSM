#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import xml.etree.ElementTree as ET
from collections import defaultdict
import pprint

#get element from main query
def get_element(filename, tags=('node', 'way', 'relation')):
    context = ET.iterparse(filename, events=('start', 'end'))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()

#OSM extract
OSM_FILE = open('Chattanooga_OSM.osm', 'r')

expectedcities = ['Chattanooga']

def is_city(element):
    return element.attrib['k'] == "addr:city"
    
cities = set()

#find all city names that are not 'Chattanooga'
def get_city_name():
    for element in get_element(OSM_FILE):
        if element.tag == "node" or element.tag == "way":
            for tag in element.iter("tag"):
                if is_city(tag):
                    if tag.attrib['v'] not in expectedcities:
                        cities.add(tag.attrib['v'])
    pprint.pprint(cities)

get_city_name()

