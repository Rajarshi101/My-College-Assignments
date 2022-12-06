"""
Question: Python program to convert a time from 12 hour to 24 hour format.
"""

'''
---::Source Code::---
'''
t =input("Enter a time in 12 Hours format (i.e., HH:MM:SS AM/PM): ")
if t[-2:] == "AM" and t[:2] == "12":
  T = "00" + t[2:-2]
elif t[-2:] == "PM" and t[:2] == "12":
  T = t[:-2]
elif t[-2:] == "AM":
  T = t[:-2]
else:
  T = str(int(t[:2]) + 12) + t[2:-2]
print("\nThe time in 24 Hours format is:",T)

'''
---::Output::---
>>> Enter a time in 12 Hours format (i.e., HH:MM:SS AM/PM): 05:23:45 PM

The time in 24 Hours format is: 17:23:45

'''
