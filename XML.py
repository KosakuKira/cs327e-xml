from xml.etree.ElementTree import Element, fromstring
#import xml.etree.ElementTree as ET

#tree = ET.parse('ElementTree.xml')
#root = tree.getroot()

print("ElementTree.py")
print()

s = "<xml>" + "".join(open("ElementTree.xml")) + "</xml>"
assert(type(s) is str)
# print(s)
print()

x = fromstring(s)
assert(type(x) is Element)

for child in x:
    print(child.tag)

print (x.findall('THU'))
print (x.tag)
print (x.iter())
print (x.findall("./red"))
print (x.findall("./THU/Team/Cooly"))
someList = x.findall("./Team/Cooly")
print (len(someList))
#xRoot = x.getroot()

#print (xRoot)
#print (xRoot.toString())




"""
ElementTree.py

<xml><THU>
	<Team>
		<ACRush></ACRush>
		<Jelly></Jelly>
		<Cooly></Cooly>
	</Team>
	<JiaJia>
		<Team>
			<Ahyangyi></Ahyangyi>
			<Dragon></Dragon>
			<Cooly><Amber></Amber></Cooly>
		</Team>
	</JiaJia>
</THU>
<Team><Cooly></Cooly></Team>

<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>
<Team><Cooly></Cooly></Team>

<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>

<red>
    <green>
        <blue></blue>
        <yellow></yellow>
    </green>
</red>
<red><green></green></red>

<red>
    <green>
        <blue></blue>
        <yellow></yellow>
    </green>
</red>
<red><blue></blue></red>

<red>
    <green>
        <blue></blue>
        <yellow></yellow>
    </green>
</red>
<red><yellow></yellow></red>

<red>
    <green>
        <blue></blue>
        <yellow></yellow>
    </green>
</red>
<green><blue></blue></green>

<red>
    <green>
        <blue></blue>
        <yellow></yellow>
    </green>
</red>
<green><yellow></yellow></green>

<red>
    <green>
        <blue></blue>
        <yellow></yellow>
    </green>
</red>
<green><purple></purple></green>
</xml>

First LeveL Elements

<Element 'THU' at 0x109e516d8>
<Element 'Team' at 0x109e51c00>
<Element 'THU' at 0x109e51cb0>
<Element 'Team' at 0x109e550a8>
<Element 'THU' at 0x109e55158>
<Element 'Team' at 0x109e55520>
<Element 'red' at 0x109e555d0>
<Element 'red' at 0x109e55730>
<Element 'red' at 0x109e557e0>
<Element 'red' at 0x109e55940>
<Element 'red' at 0x109e559f0>
<Element 'red' at 0x109e55b50>
<Element 'red' at 0x109e55c00>
<Element 'green' at 0x109e55d60>
<Element 'red' at 0x109e55e10>
<Element 'green' at 0x109e55f70>
<Element 'red' at 0x109e58050>
<Element 'green' at 0x109e581b0>

Second Level Elements

<Element 'Team' at 0x109e51788>
<Element 'JiaJia' at 0x109e51940>
<Element 'Cooly' at 0x109e51c58>
<Element 'Team' at 0x109e51d08>
<Element 'JiaJia' at 0x109e51e68>
<Element 'Cooly' at 0x109e55100>
<Element 'Team' at 0x109e551b0>
<Element 'JiaJia' at 0x109e55310>
<Element 'Cooly' at 0x109e55578>
<Element 'green' at 0x109e55628>
<Element 'green' at 0x109e55788>
<Element 'green' at 0x109e55838>
<Element 'blue' at 0x109e55998>
<Element 'green' at 0x109e55a48>
<Element 'yellow' at 0x109e55ba8>
<Element 'green' at 0x109e55c58>
<Element 'blue' at 0x109e55db8>
<Element 'green' at 0x109e55e68>
<Element 'yellow' at 0x109e55fc8>
<Element 'green' at 0x109e580a8>
<Element 'purple' at 0x109e58208>

Third Level Elements

<Element 'ACRush' at 0x109e51838>
<Element 'Jelly' at 0x109e51890>
<Element 'Cooly' at 0x109e518e8>
<Element 'Team' at 0x109e51998>
<Element 'ACRush' at 0x109e51d60>
<Element 'Jelly' at 0x109e51db8>
<Element 'Cooly' at 0x109e51e10>
<Element 'Team' at 0x109e51ec0>
<Element 'ACRush' at 0x109e55208>
<Element 'Jelly' at 0x109e55260>
<Element 'Cooly' at 0x109e552b8>
<Element 'Team' at 0x109e55368>
<Element 'blue' at 0x109e55680>
<Element 'yellow' at 0x109e556d8>
<Element 'blue' at 0x109e55890>
<Element 'yellow' at 0x109e558e8>
<Element 'blue' at 0x109e55aa0>
<Element 'yellow' at 0x109e55af8>
<Element 'blue' at 0x109e55cb0>
<Element 'yellow' at 0x109e55d08>
<Element 'blue' at 0x109e55ec0>
<Element 'yellow' at 0x109e55f18>
<Element 'blue' at 0x109e58100>
<Element 'yellow' at 0x109e58158>

Done.
"""
