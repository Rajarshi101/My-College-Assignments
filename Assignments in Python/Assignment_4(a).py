"""
Question: Python program to print reverse of a given numbers.
"""
'''
---::Source Code::---
'''
num = int(input("Enter a number: "))
newnum = 0
temp = num
while temp>0:
  rem = int(temp%10)
  newnum = (newnum*10)+rem
  temp = temp//10
print("\nThe reverse of",num,"is:",newnum)
'''
---::Output::---
>>> Enter a number: 123

The reverse of 123 is: 321
'''
