from xml.etree.ElementTree import Element, fromstring
#import xml.etree.ElementTree as ET
#tree = ET.parse('ElementTree.xml')
#root = tree.getroot()

def xml_read():
    s = "<xml>" + "".join(open("ElementTree.xml")) + "</xml>"
    assert(type(s) is str)
    x = fromstring(s)
    return x
    # assert(type(x) is Element)

# whatsiblings = [x[1]]

class StoreGlob1():   # Store globals. everytime you call, it reinitializes
    def __init__(self,x):
    #    self.startPatTag = x[-1] # first element of pattern
        self.curPattern = [x[-1]]
        self.PatCount = 0
        self.whatparents = []

def xml_findPattern(globals1,x):
    # global whatsiblings
    for child in x:
        globals1.curPattern.append(child)
        globals1.whatparents.append(x)
        globals1.PatCount += 1
      # if child is x[0]:
      # whatsiblings.append(x.findall("./*")) #all xs children)
        xml_findPattern(globals1, child)

#print("What parents?")
#print(whatparents)

##print(x.findall("./Team/Cooly"))
##print(x.findall("./THU/Team/ACRush"))
# #print(curPattern[0].findall(".//*")) #finds all that are children or grandchildren
# #print(curPattern[1].findall(".//" + curPattern[2].tag) != [])#sibling finder

##print(curPattern[0].tag)
##print(curPattern[1].tag, whatparents[0].tag)
##print(curPattern[2].tag, whatparents[1].tag)
##print(curPattern[3].tag, whatparents[2].tag)

# Doesn't work: print("Parent found is:", curPattern[patIdx-1].find('..'))
# #print("--------------------------------------------")

class StoreGlob2():   # Store globals. everytime you call, it reinitializes
    def __init__(self):
        self.hits = 0
        self.hitIdx = 0
        self.hitList = []
        self.patIdx = 0
        #    global levelIdx
        #    global searchlevelIdx

def xml_traverse (globals1,globals2, a, d = "") :
    assert(a != None)
    # print(d + a.tag)
    globals2.hits += 1
    assert(len(globals1.curPattern) > 0)

    for v in a:
        # v is a parent
        if globals2.patIdx == 0 and v.tag == globals1.curPattern[globals2.patIdx].tag: # does the traversed tag match the pattern?
            #print("Matched", curPattern[patIdx].tag, "tag. Found root.")
            globals2.hitIdx = globals2.hits
            globals2.patIdx += 1
        elif globals2.patIdx < len(globals1.curPattern)-1 and v.tag == globals1.curPattern[globals2.patIdx].tag: # matches a tag after first
            # #print("Matched", curPattern[patIdx].tag, "tag...")
            #print("Parent to find is:", whatparents[patIdx-1].tag)
            #print("Parent found is:", a.tag)
            if globals1.whatparents[globals2.patIdx-1].tag is a.tag:
                globals2.patIdx += 1
            else:
                globals2.patIdx = 0
        elif globals2.patIdx == len(globals1.curPattern)-1 and v.tag == globals1.curPattern[globals2.patIdx].tag:
            #print(numchild[patIdx - 1])
            #print("Parent to find is:", whatparents[patIdx-1].tag)
            #print("Parent found is:", a.tag)
            if globals1.whatparents[globals2.patIdx-1].tag is a.tag:
                globals2.hitList.append(globals2.hitIdx)
            globals2.patIdx = 0
            
            #print("Wow, found", curPattern[patIdx-1].tag, "end tag, saving...")
        xml_traverse(globals1,globals2,v, d + "\t")
  #  #print(d + "/" + a.tag)
# xml_traverse(x)
#print()
def xml_print(globals1):
    #print("The Grand finale!")
    print(str(len(globals1.hitList)))
    print(str(globals1.hitList))

def xml_run(filename):
    xmltree = xml_read()
    globals1 = StoreGlob1(xmltree)
    xml_findPattern(globals1,xmltree[-1])
    globals2 = StoreGlob2()
    xml_traverse(globals1,globals2,xmltree)
    globals2.hitList.pop(-1) # remove pattern since traverse picks it up
    xml_print(globals2)

xml_run("ElementTree.xml")














#print("Count: " + str(len(hitList)))
#print("Hit indices: " + str(hitList))


            #    # if a.find(".//" + curPattern[patIdx].tag) is None and curPattern[patIdx].find(".//" + curPattern[patIdx].tag):
            #    #     #print("and", curPattern[patIdx].tag, "is not beside it")
            #    #     patIdx = 0


        #            if (v.find(".//" + curPattern[patIdx].tag) is None):
#                #print("but", curPattern[patIdx].tag, "is not under it 1")
#                patIdx = 0



############
##  Previous Attempts:

# def examinefamily(a,v):
#     global patIdx
#     global patlevelIdx # what sub level in the pattern are you at
#     #print(patlevelIdx)
#   #  test = whatsiblings[patIdx-1]
#   #  #print(whatsiblings[patlevelIdx])
#     #print(curPattern[patIdx-1])
#
#     if whatparents[patIdx-1].tag == curPattern[patIdx-1].tag: #check for parent
#
#         #print("Parent is", whatparents[patIdx-1].tag, "and child is", curPattern[patIdx].tag)
#         if a.find(".//" + curPattern[patIdx].tag) is None: # there is not a match
#             #print("No Match. Restart.")
#             patIdx = 0
#             patlevelIdx = 0
#         else:
#             #print("Match.")
#             patIdx += 1
#             patlevelIdx +=1
#     elif curPattern[patIdx-1] in whatsiblings[patlevelIdx-1]:
#         #print(curPattern[patIdx-1].tag, "and", curPattern[patIdx].tag, "are siblings.")
#         #print("Both have parent", whatparents[patIdx-1].tag)
#         if a.find(".//" + curPattern[patIdx].tag) is None:# there is not a match
#             #print("No Match. Restart.")
#             patIdx = 0
#             patlevelIdx = 0
#         else:
#             #print("Match")
#             patIdx +=1
#             # patlevelIdx <- leave alone because it is a sibling
#     else:
#         #print("Error?!! D:")
#         patIdx = 0
#
# def examinefamily2(a,v):
#     global patIdx
#
#     #print(whatsiblings[patIdx-1])
#     #print(curPattern[patIdx-1])
#     if whatparents[patIdx-1].tag == curPattern[patIdx-1].tag: #check for parent
#         #print("Future: Parent is", whatparents[patIdx-1].tag, "and child is", curPattern[patIdx].tag)
#         if v.find(".//" + curPattern[patIdx].tag) is None:# there is not a match
#             #print("Future: no Match. Restart.")
#             patIdx = 0
#        # else:
#             #print("Future: Match")
#     elif curPattern[patIdx-1] in whatsiblings[patIdx-1]:
#         #print("GREAT")
#         #print("Future:", curPattern[patIdx-1].tag, "and", curPattern[patIdx].tag, "are siblings with parent", whatparents[patIdx-1].tag)
#         if a.find("./" + curPattern[patIdx].tag) is None: # Note: this only finds immediate siblings
#             #print("Future: No Match. Restart.")
#             patIdx = 0
#         #else:
#             #print("Future: Match")
#     else:
#         #print("Future Error D:")
#         patIdx = 0

#for child in x:
    #b = ""
    #Remains of old algorithm below
    #Algorithm was naive and unsuccessful

    #if(child.tag is not curPattern[0].tag):
     #   #print(child.tag)
      #  #print(curPattern[0].tag)
       # #print("Something A")
        ##print()

    ##print(child.tag)
    ##print("This is child: " + str(child.tag))
    # #print(child.find(curPattern[0].tag))
    #if (child.find(curPattern[0].tag) is None):
     #   #print(child.tag)
      #  #print(curPattern[0].tag)
        ##print(child.find(curPattern[0].tag))
       # #print("Something B")
        ##print()

    ##print ("Birde: " + str(child.find(curPattern[0].tag)))
    #if (child.tag is not curPattern[0].tag) and (child.find(curPattern[0].tag) is None):
     #   #print(child.find(curPattern[0].tag))
      #  #print("Doge")
       # b = 1
        # Junk code.
        # First tag in pattern is obviously not here.
    #else:
     #   a = 2
      #  newChild = child.find(curPattern[0].tag)
       # newCheck = newChild.find(curPattern[1].tag)
        #if (newCheck is None):
         #   #print("Such plot")
          #  c = 3
            # More junk code.
            # Pattern doesn't exist.
        #else:
         #   #print("Comic sans")
          #  occurs += 1
           # #print("Reached this occurrence")

    ##print("End of loop")



# Below was making a list of the tags in x.iter
# Whenever the tag appeared, regardless of nesting
# It would #print it
#for blah in x.iter('Cooly'):
    ##print (blah.tag)

# Testing the findall methods
##print()
##print (x.findall('THU'))
##print (x.findall('Team'))
##print()


#thu = x.findall('THU') # Outer THU tag. Still element.
#team = thu[0].findall('Team') # Found 'Team' tag within THU. Still an element.

##print(thu[0].findall('Hrrnn')) # No 'Hrrnn' tags within THU.
#teamChild1 = team[0].find('Hoenn') # No 'Hoenn' tags within Team
#teamChild2 = team[0].find('Cooly') # Found 1 Cooly tag within Team

##print(teamChild1)
##print(teamChild2)
##print()

##print(thu)
##print(team)
##print()
##print (x.tag)
##print (x.iter())
##print (x.findall("./red"))
##print (x.findall("./THU/Team/Cooly"))
#someList = x.findall("./Team/Cooly")

#findTerm = "./"
# Will be used for a much more flexible find
# Find to be used for generating the first number in the output
# i.e. the number of occurrences.

##print (someList)
##print (len(someList))
#xRoot = x.getroot()

##print (xRoot)
##print (xRoot.toString())
