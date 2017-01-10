
from lxml import html
from lxml import etree
from lxml import objectify
import re
filepath  = r'J:\Users\jeff\Downloads\Jerry\01 Fuji Pro 400H-look\22-105739-2710.xmp'
def stripnamespace(x):
    m = re.match('{.*}(.*)',x)
    if m:
        return m.group(1)
    else:
        return x

def replaceattribute(x,attribute,newstring):
    splits = attribute.split(":");   
    t = nsmap[splits[0]]
    old = x.attrib["{"+t+"}"+splits[1]]
    x.attrib["{"+t+"}"+splits[1]] = newstring
    pass


with open(filepath, 'r') as myfile:
    data=myfile.read().replace('\n', '')

nsmap = {}
tree=etree.parse(filepath)

for elem in tree.iter():
     #print(elem)
     #print(elem.nsmap)
     nsmap.update(elem.nsmap)
description = tree.xpath('//x:xmpmeta//rdf:RDF//rdf:Description',namespaces = nsmap)[0]
replaceattribute(description,"tiff:Make","New Camera")
for key, value in description.attrib.items():    
    print(stripnamespace(key),"   ",value);

for child in description:
     print(stripnamespace(child.tag))

tree.write("new.xml")










