#!/bin/python

#####
## Sample Python Exercise for WIC Programming Workshop
## November 2016
## Katherine Lynch
## If-Else

print("Pick a number between 1 and 10.")

number = int(raw_input())

if number > 10:
 print("Your number is greater than 10.")
elif number <= 10 and number > 0:
 print("Your number is between 1 and 10.")
else:
 print("Your number is less than 1.")
