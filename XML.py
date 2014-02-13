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
tagList = [x[-1]]

print (startPatTag)
print (startPatTag.find("Cooly"))
print (startPatTag.find("Amber"))
print ("Let's have some fun")
print (startPatTag)
print (startPatTag.find("./Cooly"))
print (startPatTag.find("./Cooly/Amber"))

print (startPatTag.find("Disney")) #Should return none
#print (startPatTag.findall(".//"))
print("Blackalicious")



print()

print (x)
print("Rhythm Sticksssss")
print()
#numchild = []

def tagFill(x):
 #   global numchild
  #  numchild.append(len(x)) # last one will be 0

   for child in x:
        tagList.append(child)

     #   numchild.append
        tagFill(child)

tagFill(x[-1]) # grab full pattern

print()
print(tagList)
print("Hey ese...")
print("You loco??")
print()

# print(tagList[0].tag)
# print(tagList[0].findall(".//*")) #finds all that are children or grandchildren
# print(tagList[0].findall(".//" + tagList[1].tag)) #finds all that are children or grandchildren
# print(tagList[1].findall(".//" + tagList[2].tag) != [])#sibling finder


# print(numchild) # structure of pattern

hits = 0
hitList = []

patIdx = 0
#print(type(tagList[0]))
#print(tagList[0].tag) # test for 3 that it's working
#print(tagList[1].tag)
#print(tagList[2].tag)

def traverse (a, d = "") :
    assert(a != None)
    global hits
    global hitIdx
    global patIdx
    global hitList
    global occurs

    print(d + a.tag)
    hits += 1

    #indexCatcher = []
    #firstIndex = []

    #assert(len(tagList) > 0)
    for v in a:
        if patIdx == len(tagList):
            hitList.append(hitIdx)
            patIdx = 0
            print("Pattern COMPREET")
            #Pattern was found because patIdx == length of pattern
            #Store the index of the first tag in the pattern
            #patIdx has to be reset to avoid errors.
            #This is done before any sort of searching or deeper traversal
            #Since traverse will keep returning to the first if statement
            #This conditional will check, BEFORE any searching is made
            #if this is true
        if (v.tag == startPatTag.tag):
            #v.tag is the first tag in the pattern.
            print("found", v.tag, "tag")
            print("Let's get down to business!")
            hitIdx = hits
            patIdx += 1




            #patIdx += 1

            #if (v.find(".//" + startPatTag.find()) is None):
             #   print("but", tagList[patIdx].tag, "is not under it 1")
              #  patIdx = 0
        elif (startPatTag.find(v.tag) is not None):
            #v.tag is not the first tag in the pattern
            #v.tag is the first tag's child.
            print("found child tag: ", v.tag)
            patIdx += 1
            print("To defeat, the Huns!")

        elif (startPatTag.findall(".//" + v.tag) != []):
            #v.tag is not the first tag in the pattern.
            #v.tag is not the first tag's child.
            #v.tag is a confirmed DESCENDANT of the first tag.
            patIdx += 1
            print("found descendant tag:", v.tag)
            print("You're the saddest bunch I've ever met")
        else:
            #v.tag is not the first tag in the pattern.
            #v.tag is not the first tag's child.
            #v.tag is not a confirmed DESCENDANT of the first tag.
            #Stop looking.


            patIdx = 0
            print("Pattern NO GOODE")
            #Pattern was not found.
            #patIdx must be reset anyway.
            #If we got here,
            #It probably means that the search
            #Did not yield the complete pattern.

            print(v.tag + " doesn't exist.")
            print("GET OUTTA THERE!")
            print()
        #elif patIdx < len(tagList)-1 and v.tag == tagList[patIdx].tag:
         #   print("found", tagList[patIdx].tag, "tag")
            # print(numchild[patIdx-1])
          #  patIdx += 1
           # print("comparing",  tagList[patIdx-1].tag, "and", tagList[patIdx].tag)

            #if tagList[patIdx-1].findall(".//" + tagList[patIdx].tag) == []: # if empty, not parent
             #   print(tagList[patIdx].tag, "We are looking for a sibling!")
              #  if (v.find(".//" + tagList[patIdx].tag) is None):   # if not a sibling
               #     print("but", tagList[patIdx].tag, "is not a sibling")
                #    patIdx = 0
                #if a.findall(".//" + tagList[patIdx].tag) != []: # found a sibling!
                 #   print(tagList[patIdx].tag, "<- sibling!")
                #else:
                 #   patIdx = 0
                #  do sibling things
                # a.find(".//" + tagList[patIdx].tag)

            #elif (v.find(".//" + tagList[patIdx].tag) is None):   # if not a sibling
             #   print("but", tagList[patIdx].tag, "is not under it 2")
              #  patIdx = 0

               # if a.find(".//" + tagList[patIdx].tag) is None and tagList[patIdx].find(".//" + tagList[patIdx].tag):
               #     print("and", tagList[patIdx].tag, "is not beside it")
               #     patIdx = 0

        #elif patIdx == len(tagList)-1 and v.tag == tagList[patIdx].tag:
           # print(numchild[patIdx - 1])
         #   print("found", tagList[patIdx].tag, "end tag, saving...")
          #  patIdx = 0
           # hitList.append(hitIdx)

        #indexCatcher.append(hits)
        #if (patIdx < len(tagList)):
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

   # print(d + "/" + a.tag)
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

    #if(child.tag is not tagList[0].tag):
     #   print(child.tag)
      #  print(tagList[0].tag)
       # print("Something A")
        #print()

    #print(child.tag)
    #print("This is child: " + str(child.tag))
    # print(child.find(tagList[0].tag))
    #if (child.find(tagList[0].tag) is None):
     #   print(child.tag)
      #  print(tagList[0].tag)
        #print(child.find(tagList[0].tag))
       # print("Something B")
        #print()

    #print ("Birde: " + str(child.find(tagList[0].tag)))
    #if (child.tag is not tagList[0].tag) and (child.find(tagList[0].tag) is None):
     #   print(child.find(tagList[0].tag))
      #  print("Doge")
       # b = 1
        # Junk code.
        # First tag in pattern is obviously not here.
    #else:
     #   a = 2
      #  newChild = child.find(tagList[0].tag)
       # newCheck = newChild.find(tagList[1].tag)
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
