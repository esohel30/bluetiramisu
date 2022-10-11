'''
Team Brown: Nakib Abedin, Eric Sohel, Shafiul Haque
SoftDev pd08
K07 - TEARDOWN
2022-09-22
time spent: 0.5hrs
'''

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go? goes in the shell after you click the link, provided debug is false
    return "No hablo queso!"

app.debug = True
app.run()