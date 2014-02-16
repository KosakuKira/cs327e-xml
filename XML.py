from xml.etree.ElementTree import Element, fromstring

def xml_read(filename):
    """
    Reads from the XML file.
    filename is the XML file.
    """
    s = "<xml>" + "".join(open(filename)) + "</xml>"
    type(s)
    assert(type(s) is str)
    x = fromstring(s)
    return x
class StoreGlob1():
    """
    Store globals
    Everytime you call, it reinitializes
    """
    def __init__(self,x):
        self.curPattern = [x[-1]]
        self.PatCount = 0
        self.whatparents = []

def xml_findPattern(globals1,x):
    """
    Finds the pattern and stores it
    """
    for child in x:
        globals1.curPattern.append(child)
        globals1.whatparents.append(x)
        globals1.PatCount += 1
        xml_findPattern(globals1, child)

class StoreGlob2():
    """
    Store globals
    Everytime you call, it reinitializes
    """
    def __init__(self):
        self.hits = 0
        self.hitIdx = 0
        self.hitList = []
        self.patIdx = 0

def xml_traverse (globals1,globals2, a, d = "") :
    """
    Modified version of Downing's traverse()
    Made to work with program
    """
    assert(a != None)
    globals2.hits += 1
    assert(len(globals1.curPattern) > 0)

    for v in a:
        if globals2.patIdx == 0 and v.tag == globals1.curPattern[globals2.patIdx].tag: # does the traversed tag match the pattern?
            globals2.hitIdx = globals2.hits
            globals2.patIdx += 1
        elif globals2.patIdx < len(globals1.curPattern)-1 and v.tag == globals1.curPattern[globals2.patIdx].tag: # matches a tag after first

            if globals1.whatparents[globals2.patIdx-1].tag is a.tag:
                globals2.patIdx += 1
            else:
                globals2.patIdx = 0
        elif globals2.patIdx == len(globals1.curPattern)-1 and v.tag == globals1.curPattern[globals2.patIdx].tag:
            if globals1.whatparents[globals2.patIdx-1].tag is a.tag:
                globals2.hitList.append(globals2.hitIdx)
            globals2.patIdx = 0

        xml_traverse(globals1,globals2,v, d + "\t")
   #print(d + "/" + a.tag)
def xml_print(globals1):
    """
    Helper function
    Prints the occurrences
    And the indices

    Not to be used alone
    But used with xml_solve()
    """

    print(len(globals1.hitList))
    for hit in globals1.hitList:
        print(hit)

def xml_solve(filename):
    """
    Runs the entire operation.
    """
    xmltree = xml_read(filename)
    globals1 = StoreGlob1(xmltree)
    xml_findPattern(globals1,xmltree[-1])
    globals2 = StoreGlob2()
    xml_traverse(globals1,globals2,xmltree)
    globals2.hitList.pop(-1) # remove pattern since traverse picks it up
    xml_print(globals2)

# xml_solve("ElementTree.xml")










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
