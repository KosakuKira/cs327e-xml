
from xml.etree.ElementTree import Element, fromstring

s = "<xml>" + "".join(open("ElementTree.xml")) + "</xml>"
assert(type(s) is str)

x = fromstring(s)
# assert(type(x) is Element) # assertion error on Mandy's computer but still works as an element

startPatTag = x[-1] # first element of pattern
curPattern = [x[-1]]
def findPattern(x):
    for child in x:
        curPattern.append(child)
        findPattern(child)

findPattern(x[-1]) # grab full pattern

print("Pattern found:", curPattern)
hits = 0
hitList = []
patIdx = 0
taglist = []

def traverse (a, d = ""):
    assert(a != None)
    global hits
    global patIdx
    global hitList
    global hitIdx
    hits += 1
    #print(d + a.tag)
    global taglist
    assert(len(curPattern) > 0)

    for v in a:
        print("tags:", taglist)
        childrenleft = len(v)

        if (a.find(".//" + curPattern[patIdx].tag) is None):  # Reset if the element to find is not a sub element
            print("couldn't find", curPattern[patIdx].tag, "under", a.tag)
            patIdx = 0
            taglist = []
        elif v.find(".//" + curPattern[patIdx].tag) is None and curPattern[patIdx].tag is not v.tag:  # Reset if the element to find is not a sub element
            print("I couldn't find", curPattern[patIdx].tag, "under", v.tag)
            taglist = []

        else: # tag is found
            print("found", curPattern[patIdx].tag, "under", a.tag)
            taglist.append(curPattern[patIdx].tag)

        if patIdx == 0 and v.tag == curPattern[patIdx].tag: # does the traversed tag match the pattern?
                print("found", curPattern[patIdx].tag, "tag")
                hitIdx = hits
                patIdx += 1
                if (v.find(".//" + curPattern[patIdx].tag) is None):
                    print(v.tag, "it's not in there")
                    patIdx = 0
                    tagList = []

        elif patIdx < len(curPattern)-1 and v.tag == curPattern[patIdx].tag:
                print("found", curPattern[patIdx].tag, "tag")
                patIdx += 1
                if (v.find(".//" + curPattern[patIdx].tag) is None):
                    print("but", curPattern[patIdx].tag, "is not under it")
                    patIdx = 0
                    tagList = []
        elif patIdx == len(curPattern)-1 and v.tag == curPattern[patIdx].tag:
                print("found", curPattern[patIdx].tag, "end tag, saving...")
                patIdx = 0
                hitList.append(hitIdx)

        traverse(v, d + "\t")

   # print(d + "/" + a.tag)

traverse(x)

print()
hitList.pop(-1) # remove pattern since traverse picks it up

print("The Grand finale!")
print("Count: " + str(len(hitList)))
print("Hit indices: " + str(hitList))
