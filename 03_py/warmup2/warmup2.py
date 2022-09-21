def string_times(str, n):
  return str*n

def string_splosion(str):
  var = ""
  e =0
  while e != len(str): 
    var += str[0:e]
    e+=1
  return var + str

def array_front9(nums):
  
  var = 4 
  
  if len(nums) < 4: 
    var = len(nums) 
  
  for i in range(var): 
    if(nums[i] == 9): 
      return True
  return False
  
def front_times(str, n):
  return str[0:3] * n

def last2(str):
  
  if(len(str) == 0): 
    return 0
  
  var = str[len(str) - 2: len(str)]
  counter = 0 
  
  
  for e in range (len(str)): 
    if(str[e: e+ 2] == var): 
      counter += 1 
      

  return counter-1

def array123(nums):
  
  
  for e in range(len(nums)): 
    if(nums[e] == 1): 
        for e in range(len(nums)): 
           if(nums[e] == 2): 
               for e in range(len(nums)): 
                 if(nums[e] == 3): 
                    return True
                    
                    
  
  return False
  
def string_bits(str):
  
  var = "" 
  
  for e in range(0, len(str), 2): 
    var += str[e]
    
  return var

def array_count9(nums):
  
  counter = 0 
  
  
  for e in range(len(nums)): 
    if(nums[e] == 9): 
      counter += 1
      
      
  return counter

def string_match(a, b):
  
  shorter =  0
  counter = 0 

  if(len(a) <= 1 or len(b) <= 1): 
    return 0 
    
  if(len(a) > len(b)):
    shorter = len(b)
  else:
    shorter = len(a)
    
  for e in range(shorter-1): 
    if(a[e: e+2] == b[e: e+2]): 
      counter += 1 
      
  return counter
  
