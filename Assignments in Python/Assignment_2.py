"""
Question: Python program to find factors of a given number.
"""

'''
---::Source Code::---
'''
list1 = []
num = int(input("Enter a number: "))
for i in range(1,num+1):
  if num%i==0:
    list1.append(i)
print("\nThe factors of the number",num,"are:",list1)

'''
---::Output::---
>>> Enter a number: 120

The factors of the number 120 are: [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]
'''
