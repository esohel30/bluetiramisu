'''
Team Brown: Nakib Abedin, Eric Sohel, Shafiul Haque
SoftDev pd08
K07 - TEARDOWN
2022-09-22
time spent: 0.5hrs
'''


from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?



@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
QCC: What is the @ symbol supposed to represent in the code/what is its purpose?
Does printing __name__ run the app?
0. Line 12 utilized a similar syntax as the java constructor.
1. The forward slash is utilized when we navigate directories.
2. The output will be printed in the website once the flask app is opened, with the return value printed.
3. The return value "No hablo queso!" will be printed. 
4. It will appear on the website once the flask app is opened.
5. Java has object-oriented programming, as seen on line 21 with the call of a method from app.
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''