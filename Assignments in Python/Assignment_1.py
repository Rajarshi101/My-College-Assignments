"""
Question: Python program to find the maximum number from three given numbers.
"""

'''
---::Source Code::---
'''
def maximum_of_two(x,y):
  if x>y:
    return x
  return y

def maximum_of_three(p,q,r):
  return(maximum_of_two(p,maximum_of_two(q,r)))

print("Enter three numbers:--")
a = input()
b = input()
c = input()
print("\nThe maximum number is:",maximum_of_three(a,b,c))

'''
---::Output::---
>>> Enter three numbers:--
>>> 2
>>> 8
>>> 5

The maximum number is: 8
'''
