"""
Question: Python program to compute the greatest common divisor of two given positive integers.
"""

'''
---::Source Code::---
'''
def gcd_check(x,y):
    if x==0 or y==0:
       return 0
    elif x>y:
        return gcd_cal(y,x)
    elif x<y:
        return gcd_cal(x,y)

def gcd_cal(a,b):
    for i in range(b,0,-1):
      if a%i==0 and b%i==0:
        return i
      
print("Enter two numbers:--")
num1 = int(input())
num2 = int(input())
print("\nThe G.C.D of",num1,"and",num2,"is:",gcd_check(num1,num2))

'''
---::Output::---
>>> Enter two numbers:--
>>> 120
>>> 75

The G.C.D of 120 and 75 is: 15


>>> Enter two numbers:--
>>> 0
>>> 36

The G.C.D of 0 and 36 is: 0
'''
