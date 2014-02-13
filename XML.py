from xml.etree.ElementTree import Element, fromstring
#import xml.etree.ElementTree as ET
#tree = ET.parse('ElementTree.xml')
#root = tree.getroot()

s = "<xml>" + "".join(open("ElementTree.xml")) + "</xml>"
assert(type(s) is str)
# print(s)
#print()

x = fromstring(s)
# assert(type(x) is Element)

#print(x.findall("./Team/Cooly"))
#print(x.findall("./THU/Team/ACRush"))

startPatTag = x[-1] # first element of pattern
curPattern = [x[-1]]
numchild = []
def findPattern(x):
    global numchild
    numchild.append(len(x)) # last one will be 0
    test = len(x)
    for child in x:
        test -= 1
        curPattern.append(child)
        numchild.append
        findPattern(child)

print(curPattern[0].findall(".//*"))

print("\n")
findPattern(x[-1]) # grab full pattern
print(numchild) # structure of pattern

hits = 0
hitList = []
patIdx = 0
print(type(curPattern[0]))
#print(curPattern[0].tag) # test for 3 that it's working
#print(curPattern[1].tag)
#print(curPattern[2].tag)

def traverse (a, d = "") :
    assert(a != None)
    global hits
    global hitIdx
    global patIdx
    global hitList

    print(d + a.tag)
    hits += 1

    #indexCatcher = []
    #firstIndex = []

    assert(len(curPattern) > 0)
    for v in a:
        if patIdx == 0 and v.tag == curPattern[patIdx].tag: # does the traversed tag match the pattern?
            print("found", curPattern[patIdx].tag, "tag")
            hitIdx = hits
            patIdx += 1
            if (v.find(".//" + curPattern[patIdx].tag) is None):
                print("but", curPattern[patIdx].tag, "is not under it")
               # if (a.find(".//" + curPattern[patIdx].tag) is None):
               #     print("and", curPattern[patIdx].tag, "is not beside it")
               #     patIdx = 0

        elif patIdx < len(curPattern)-1 and v.tag == curPattern[patIdx].tag:
            print("found", curPattern[patIdx].tag, "tag")
            print(numchild[patIdx-1])
            patIdx += 1

            if (v.find(".//" + curPattern[patIdx].tag) is None):
                print("but", curPattern[patIdx].tag, "is not under it")
                patIdx = 0
                #if a.find(".//" + curPattern[patIdx].tag) is None and curPattern[patIdx].find(".//" + curPattern[patIdx].tag):
               #     print("and", curPattern[patIdx].tag, "is not beside it")
               #     patIdx = 0

        elif patIdx == len(curPattern)-1 and v.tag == curPattern[patIdx].tag:
            print(numchild[patIdx - 1])
            print("found", curPattern[patIdx].tag, "end tag, saving...")
            patIdx = 0
            hitList.append(hitIdx)

        #indexCatcher.append(hits)
        #if (patIdx < len(curPattern)):
           # hitList.append(hits)
        #patIdx += 1
#        hitList.append(hits)
    #else:
     #   patIdx = 0

        #firstIndex.append(indexCatcher[0])
        #indexCatcher = []
        #hitList.append(hits)

    #if hits == 1:
     #   occurs += 1
        #hits += 1
        #if (v.tag == check1):
            #occurs += 1
            #hitList.append(hits)
        #if (v.tag == check1):
         #   hits += 1
        #elif (a.tag == check2):
            #hits += 1

        #if hits == 1:
         #   occurs += 1
        traverse(v, d + "\t")

    print(d + "/" + a.tag)
traverse(x)

print()
# hitList.pop(-1) # remove pattern since traverse picks it up

print("The Grand finale!")
print("Count: " + str(len(hitList)))
print("Hit indices: " + str(hitList))

# Previous Attempts:

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
#someList = x.findall("./Team/Cooly")

#findTerm = "./"
# Will be used for a much more flexible find
# Find to be used for generating the first number in the output
# i.e. the number of occurrences.

#print (someList)
#print (len(someList))
#xRoot = x.getroot()

#print (xRoot)
#print (xRoot.toString())
