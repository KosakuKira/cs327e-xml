#!/usr/bin/env python3

# --------------
# ElementTree.py
# --------------

from xml.etree.ElementTree import Element, fromstring, tostring

print("ElementTree.py")
print()

def traverse (a, d = "") :
    print(d + a.tag)
    for v in a :
        traverse(v, d + "\t")
    print(d + "/" + a.tag)

s = "<xml>" + "".join(open("ElementTree.xml")) + "</xml>"
assert(type(s) is str)

a = fromstring(s)
assert(type(a) is Element)

traverse(a)
print()

print("Done.")

"""
ElementTree.py

xml
	THU
		Team
			ACRush
			/ACRush
			Jelly
			/Jelly
			Cooly
			/Cooly
		/Team
		JiaJia
			Team
				Ahyangyi
				/Ahyangyi
				Dragon
				/Dragon
				Cooly
					Amber
					/Amber
				/Cooly
			/Team
		/JiaJia
	/THU
	Team
		Cooly
		/Cooly
	/Team
/xml

Done.
"""
