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

evenNum = 0
patterns = []
for child in x:
    print(child.tag)
    evenNum += 1
    if ((evenNum % 2) == 0):
        patterns.append(child)

print (patterns)
print (patterns[0].tag)

curPattern = []
curPattern.append(patterns[0])
for child in patterns[0]:
    print (child.tag)
    curPattern.append(child)

print (curPattern)

occurs = 0
hits = 0

check1 = curPattern[0].tag
check2 = curPattern[1].tag

def traverse (a, occurs, d = "") :
    print(d + a.tag)
    hits = 0
    if (a.tag == check1):
        hits += 1
    #elif (a.tag == check2):
        #hits += 1

    if hits == 1:
        occurs += 1
    for v in a:
        if (v.tag == check1):
            hits += 1
        #elif (a.tag == check2):
            #hits += 1

        if hits == 1:
            occurs += 1
        traverse(v, occurs, d + "\t")
    print(d + "/" + a.tag)


traverse(x, occurs)

#for child in x:

    #b = ""

    #Remains of old algorithm below
    #Algorithm was naive and unsuccessful

    #if(child.tag is not curPattern[0].tag):
     #   print(child.tag)
      #  print(curPattern[0].tag)
       # print("Something A")
        #print()

    #print(child.tag)
    #print("This is child: " + str(child.tag))
    # print(child.find(curPattern[0].tag))
    #if (child.find(curPattern[0].tag) is None):
     #   print(child.tag)
      #  print(curPattern[0].tag)
        #print(child.find(curPattern[0].tag))
       # print("Something B")
        #print()



    #print ("Birde: " + str(child.find(curPattern[0].tag)))
    #if (child.tag is not curPattern[0].tag) and (child.find(curPattern[0].tag) is None):
     #   print(child.find(curPattern[0].tag))
      #  print("Doge")
       # b = 1
        # Junk code.
        # First tag in pattern is obviously not here.
    #else:
     #   a = 2
      #  newChild = child.find(curPattern[0].tag)
       # newCheck = newChild.find(curPattern[1].tag)
        #if (newCheck is None):
         #   print("Such plot")
          #  c = 3
            # More junk code.
            # Pattern doesn't exist.
        #else:
         #   print("Comic sans")
          #  occurs += 1
           # print("Reached this occurrence")

    #print("End of loop")

print()
print("The Grand finale!")
print("Count: " + str(occurs))



# Below was making a list of the tags in x.iter
# Whenever the tag appeared, regardless of nesting
# It would print it
#for blah in x.iter('Cooly'):
    #print (blah.tag)

# Testing the findall methods
#print()
#print (x.findall('THU'))
#print (x.findall('Team'))
#print()


#thu = x.findall('THU') # Outer THU tag. Still element.
#team = thu[0].findall('Team') # Found 'Team' tag within THU. Still an element.

#print(thu[0].findall('Hrrnn')) # No 'Hrrnn' tags within THU.
#teamChild1 = team[0].find('Hoenn') # No 'Hoenn' tags within Team
#teamChild2 = team[0].find('Cooly') # Found 1 Cooly tag within Team



#print(teamChild1)
#print(teamChild2)
#print()



#print(thu)
#print(team)
#print()
#print (x.tag)
#print (x.iter())
#print (x.findall("./red"))
#print (x.findall("./THU/Team/Cooly"))
someList = x.findall("./Team/Cooly")

findTerm = "./"
# Will be used for a much more flexible find
# Find to be used for generating the first number in the output
# i.e. the number of occurrences.

print (someList)
print (len(someList))
#xRoot = x.getroot()

#print (xRoot)
#print (xRoot.toString())

