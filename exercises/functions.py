#!/bin/python

#####
## Sample Python Exercise for WIC Programming Workshop
## November 2017
## Katherine Lynch
## Functions

def transform_name(name):
  formatted_name  = name.strip().title()
  return formatted_name

def get_name(name_type):
  print("Hi, what is your {} name?").format(name_type)
  name = raw_input()
  return name

f_name = get_name("first")
f_name = transform_name(f_name)

print("Hi " + f_name)

m_name = get_name("middle")
m_name = transform_name(m_name)

print("Nice, " + m_name)

l_name = get_name("last")
l_name = transform_name(l_name)

print("Hello, {first} {middle} {last}!").format(first = f_name, middle = m_name, last = l_name)
