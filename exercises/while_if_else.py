#!/bin/python

#####
## Sample Python Exercise for WIC Programming Workshop
## November 2016
## Katherine Lynch
## While / If-Else

print("Guess how many pounds the biggest ball of twine weighs?")
total = 19973

while True:
  guess = int(raw_input())
  if guess > total:
    print( "Too high!")
  elif guess < total:
    print("Too low!")
  else:
    print("You guessed it!")
    break
