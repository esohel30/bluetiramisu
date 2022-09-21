def sleep_in(weekday, vacation):

  if weekday and vacation:
    return True
  elif vacation:
    return True
  elif  not weekday and  not vacation:
    return True
  elif weekday:
    return False
  
def diff21(n):
  if(n > 21):
    return 2 * abs(n-21)
  else:
    return abs(n-21)

def near_hundred(n):
  if( abs(100 -n) <= 10 or abs( 200 - n) <= 10):
    return True 
  else:
    return False

def missing_char(str, n):
  return str[0: n] + str[n+1: len(str)]
  
def monkey_trouble(a_smile, b_smile):
  if( a_smile and b_smile):
    return True 
  elif( not a_smile and not b_smile):
    return True 
  else:
    return False

def parrot_trouble(talking, hour):
  if(talking and (hour < 7 or hour > 20)):
    return True 
  else:
    return False

def pos_neg(a, b, negative):
  if( negative):
    return a < 0 and b < 0
  elif (a * b < 0):
    return True
  else: 
    return False

def front_back(str):
  if(len(str) == 1):
    return str
  else:
    return str[ len(str)-1: len(str)] + str[1:len(str) - 1] + str[0:1]

def sum_double(a, b):
  
  if(a == b):
    return 2 * (a+b)
  else:
    return a + b

def makes10(a, b):
  return (a == 10 or b == 10) or (a+b == 10)
  
  
def not_string(str):
  if(str == "not"):
    return str 
  elif(str[0:4] == "not "):
    return str
  else: 
    return "not " + str

def front3(str):
  if(len(str) < 3):
    return str*3
  else:
    return str[0:3]*3





