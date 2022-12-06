"""
Question: Python program to takes your name as input, remove all vowels from your name and display the resultant string.
"""

'''
---::Source Code::---
'''
list1 = ['a','e','i','o','u','A','E','I','O','U']
name = input("Enter your name: ")
Name = ''
for i in name:
  if i not in list1:
    Name += name
print("Your name without vowels is:",Name)

'''
---::Output::---
>>> Enter your name: Rajarshi
Your name without vowels is: Rjrsh
'''
