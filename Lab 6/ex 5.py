# Write another variant of the function from the previous exercise 
# that returns those elements that have at least one attribute that corresponds to a key-value pair in the dictionary

import xml.etree.ElementTree as ET
def xml_function(path, attrs):
    tree = ET.parse(path)
    root = tree.getroot()
    elements = []
    for child in root:
        ok = False
        for key in attrs:
            if child.attrib.get(key) == attrs[key]: 
                ok = True
        if ok:
            elements.append(child.tag)
    return elements           

print (xml_function("data.xml", {"class": "url", "name": "url-form", "data-id": "item"}))
