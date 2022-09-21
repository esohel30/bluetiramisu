def first_last6(nums):
  
  return (nums[len(nums)-1] == 6 or nums[0] == 6)

def common_end(a, b):
  
  return (a[0] == b[0]) or a[len(a)-1] == b[len(b)-1]
  
  
def reverse3(nums):
  
  var = []
  
  for e in range(len(nums)-1, -1, -1):
    var.append(nums[e])
  
  
  
  return var
    
def middle_way(a, b):
  
  
  
  return [a[1], b[1]]

  
  
  
  
