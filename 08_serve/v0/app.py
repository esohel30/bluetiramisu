'''
Team Brown: Nakib Abedin, Eric Sohel, Shafiul Haque
SoftDev pd08
K07 - TEARDOWN
2022-09-22
time spent: 0.5hrs
'''

from flask import Flask
app = Flask(__name__) # constructor, creates the flask

@app.route("/") # routes the app to the link
def hello_world():
    print(__name__) # doesn't return anything
    return "No hablo queso!"  # statement prints out when you click the link

app.run()  # runs the app