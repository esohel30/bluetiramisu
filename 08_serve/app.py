'''
Team Brown: Nakib Abedin, Eric Sohel, Shafiul Haque
SoftDev pd08
K07 - TEARDOWN
2022-09-22
time spent: 0.5hrs
'''

from flask import Flask
import csv
import random as rng
# imported csv to read file, rng in the later function

def filereader():
    file1 = open("occupations.csv",'r')
    file1.readline()
    sha= file1.readlines() #skip first line bc it just has the headings, which aren't necessary
    sha = sha[:-1]
    dictionary = {} #make dictionary
    for e in sha: #two cases, if a string has " " remove it after the quotes are finished, if a string is ' ' remove it after the , is done
        if e[0] == '"':
            dictionary[e[1:e.find('",')]] = float(e[e.find('",')+2:len(e)-1])
        else:
            dictionary[e[0:e.find(',')]] = float(e[e.find(',')+1:len(e)-1])
    return dictionary

def occupation(dic):
    occlist = [] #make a list that should be filled with 998 values depending on the percentage chance of the occupation
    for key in dic: # go through each occupation
        number = int((dic[key])*10) #multiply by 10 to get a int value
        for x in range(number):
            occlist.append(key) #add the value to the occlist
    index = rng.randint(0, len(occlist)-1) #generate a random value that would be an index in the occlist
    return "Your randomly selected occupation is " + occlist[index] + " with a " + str(dic[occlist[index]]) + "% chance." #return occupation and chance
    

app = Flask(__name__) #create instance of class Flask


@app.route("/")       #assign fxn to route
def returnTNPG():
        x = "Team Brown: Nakib Abedin, Eric Sohel, Shafiul Haque<br>SoftDev pd08\nK08 - SERVE<br>2022-10-07<br>time spent: 1.1hrs<br><br>" + occupation(filereader()) + "<br><br>"
        dictx = filereader()
        for key in dictx:
            x += "<br>" + key + " " + str(dictx[key]) + "<br>"
        return x

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
