#!/bin/python

#####
## Sample Python Exercise for WIC Programming Workshop
## November 2017
## Katherine Lynch
## While

print("Guess how many pounds the biggest ball of twine weighs?")
guess = int(raw_input())

total = 19973

while guess != total:
  print("Nope!  Guess again:")
  guess = int(raw_input())

print("You guessed it!")
