"""
Question: Python program to convert a given decimal number into corresponding binary number.
"""
'''
---::Source Code::---
'''
def binary(n):
  if n>1:
    binary(n//2)
  print(n%2,end = "")
    
num = int(input("Enter a decimal number: "))
print("\nThe Binary value of the Decimal number",num,"is:",end=" ")
binary(num)
'''
---::Output::---
>>> Enter a decimal number: 13

The Binary value of the Decimal number 13 is: 1101
'''
