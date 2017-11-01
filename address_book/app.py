#!/bin/python

#####
## Sample Python Program for WIC Programming Workshop
## November 2016
## Katherine Lynch

def print_all(address_book):
  for key in sorted(address_book):
    full_name = address_book[key]["first_name"] + " " + address_book[key]["last_name"]
    details = "Contact information for {0}\nFull Name: {1}\nPhone: {2}\nEmail:{3}".format(key, full_name, address_book[key]["phone"], address_book[key]["email"])
    print "==========\n{entry}\n==========\n\n".format(entry = details.upper())

def print_one(initials, dictionary):
    print("Contact information for {0}\n").format(input)
    print(formatting(dictionary))

def formatting(dictionary):
    full_name = dictionary["first_name"] + " " + dictionary["last_name"]
    details = "Full Name: {0}\nPhone: {1}\nEmail:{2}".format(full_name, dictionary["phone"], dictionary["email"])
    return details


entries = { "KL" : { "first_name" : "Kate",
                     "last_name" : "Lynch",
                     "email" : "katherly@upenn.edu",
                     "phone" : "215-555-1234"
                   },
            "CS" : { "first_name" : "Carly",
                     "last_name" : "Sewell",
                     "email" : "carlysew@upenn.edu",
                     "phone" : "215-555-5678"
                   }
          }

commands = ["all", "exit"]

options = commands + entries.keys()

print("Welcome to your address book!")

while True:
    input = raw_input("What would you like to do?")
    if input.lower() == "all":
        print "Printing info for all contacts -- \n"
        print_all(entries)
    elif input.lower() == "exit":
        print "Goodbye!"
        break
    elif input.upper() in entries.keys():
        print_one(input, entries[input.upper()])
    else:
        print "I don't understand your command.  Options are: {0}".format(options)
