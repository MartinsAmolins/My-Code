
# import numpy module 
import numpy as np 
  
# create an array of 10 elements 
a = np.array([1, 3, 2, 4, 8, 6, 7, 34, 56, 78]) 
  
# get index 4 element address 
print("The element present at 4 th  index - element", 
      a[4], ":", a[4].data) 
  
# get index 5 element address 
print("The element present at 5 th index - element", 
      a[5], ":", a[5].data) 
  
# get index 1 element address 
print("The element present at 1 st index - element", 
      a[1], ":", a[1].data) 
  
# get index 0 element address 
print("The element present at 0 th  index - element", 
      a[0], ":", a[0].data) 