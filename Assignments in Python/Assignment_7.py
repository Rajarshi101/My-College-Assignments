"""
Question: Python program that accepts a string from the user and check whether it is a palindrome or not.
"""

'''
---::Source Code::---
'''

str1 = input("Enter a string: ")
str1 = str1.lower()
if(str1[::]==str1[::-1]):
  print("\nThe string is a Palindrome")
else:
  print("\nThe string is Not a Palindrome")

'''
---::Output::---
>>> Enter a string: madam

The string is a Palindrome

>>> Enter a string: Good

The string is Not a Palindrome

>>> Enter a string: Noon

The string is a Palindrome

'''
