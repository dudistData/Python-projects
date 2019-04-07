# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:48:55 2019

@author: wilki
"""

count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1

print ("Good bye!")

count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")

numbers = range(1,6)
for i in numbers:
    print (i)