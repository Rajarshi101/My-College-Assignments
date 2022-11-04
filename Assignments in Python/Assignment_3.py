"""
Question: Python program to compute sum of digits of a given number.
"""
'''
---::Source Code::---
'''
num = int(input("Enter a number: "))
add = 0
temp = num
while temp>0:
  rem = int(temp%10)
  add = add+rem
  temp = temp//10
print("\nThe sum of digits of",num,"is:",add)
'''
---::Output::---
>>> Enter a number: 120

The sum of digits of 120 is: 3
'''
