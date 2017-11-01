#!/bin/python

#####
## Sample Python Exercise for WIC Programming Workshop
## November 2017
## Katherine Lynch
## Hello World

print("What is your name?")

name = raw_input()

print("Hello, " + name.title() + "!")

print("Hello, {}!").format(name.title())
