# Write a function that receives as a parameter the path to an xml document and an attrs dictionary 
# and returns those elements that have as attributes all the keys in the dictionary and values ​​the corresponding values.
# For example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} 
# the items selected will be those tags whose attributes are class="url" si name="url-form" si data-id="item"
import xml.etree.ElementTree as ET

def xml_function(path, attrs):
    tree = ET.parse(path)
    root = tree.getroot() 
    elements = []
    for child in root:
        ok = True
        for key in attrs:
            if child.attrib[key] != attrs[key]: 
                ok = False
        if ok:
            elements.append(child.tag)
    return elements

print (xml_function("data.xml", {"class": "url", "name": "url-form", "data-id": "item"}))

