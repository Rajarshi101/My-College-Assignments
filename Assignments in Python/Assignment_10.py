"""
Question: Python program to check a given string contains all unique characters or not.
"""

'''
---::Source Code::---
'''
string = (input("Enter a string: ")).lower()
newstr = ''
for i in string:
  if i not in newstr:
    newstr += i
if newstr == string:
  print("String contains all unique characters")
else:
  print("String does not not contains all unique characters")

'''
---::Output::---

>>> Enter a string: abcde
String contains all unique characters

>>> Enter a string: abcde
String contains all unique characters

>>> Enter a string: AbcBa
String does not not contains all unique characters

'''
