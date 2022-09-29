"""
Eric Sohel and Wilson Mach
"""

import random

def makeDict(data):
    name = {}

    tempPeriod = ""
    tempName = ""
    tempDucky = ""

    e=0
    counter = 0

    test = ""
    acounter = 0
    while(e <= len(data)):
        if data[e:e+1] == "@" or e==len(data):
            name[tempName] = tempPeriod + ":" + tempDucky
           
            tempPeriod = ""
            tempName = ""
            tempDucky = ""
           
            counter = 0
            e+=3
            acounter+=1
        elif data[e:e+1] == "$":
            counter+=1
            e+=3
           
        else:
            if counter == 0:
                tempPeriod += data[e:e+1]
            elif counter == 1:
                tempName += data[e:e+1]
            elif counter == 2:
                tempDucky += data[e:e+1]
            test += data[e:e+1]
            e+=1
           
    return name
       
fileObject = open("krewes.txt", "r")
datas = fileObject.read()
if(len(datas) == 0):
    print(None) 
#print(datas)
periods = makeDict(datas)
#print(periods)


randomdevo = (random.choice(list(periods.keys())))

info = (periods[randomdevo])


print(randomdevo)
print(info.split(":")[0])
print(info.split(":")[1])




