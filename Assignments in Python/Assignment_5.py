"""
Question: Python program to print the following pattern using nested for loop.
          *
          * *
          * * *
          * *
          *
"""
'''
---::Source Code::---
'''
symb = input("Enter symbol: ")
n = int(input("Enter the max number of symbols in a row: "))
print()
for i in range(1,n+1):
  for j in range(1,i+1):
    print(symb,end = " ")
  print()
for i in range(n,1,-1):
  for j in range(i-1,0,-1):
    print(symb,end = " ")
  print()

'''
---::Output::---
>>> Enter symbol: *
>>> Enter the max number of symbols in a row: 6

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
