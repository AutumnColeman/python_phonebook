#You will write a command line program to manage a phone book. When you start the phonebook.py program, it will print out a menu and ask the user to enter a choice:
#If they choose to look up an entry, you will ask them for the person's name, and then look up the person's phone number by the given name and print it to the screen.
#If they choose to set an entry, you will prompt them for the person's name and the person's phone number,
#If they choose to delete an entry, you will prompt them for the person's name and delete the given person's entry.
#If they choose to list all entries, you will go through all entries in the dictionary and print each out to the terminal.
#If they choose to quit, end the program.
import pickle
from os.path import exists

if exists('phonebook.pickle'):
    # open the file in read mode (r)
    whitebook = open('phonebook.pickle', 'r')
    # load the contents from the file and store it in the phonebook_dict variable
    whitebook_dict = pickle.load(whitebook)
else:
    whitebook_dict = {}

#whitebook = {
#    "Autumn": "770-555-5555",
#    "Bob": "404-555-5555",
#    "Cat": "678-555-5555",
#    "Dog": "470-555-5555"
#}

print """
Electronic Phone Book
=====================

1\. Look up an entry
2\. Set an entry
3\. Delete an entry
4\. List all entries
5\. Save entries
6\. Quit
"""
menu_number = raw_input("What do you want to do (1-6)? ")

#Looks up an entry
if menu_number == "1":
    name = raw_input("Name? ").lower()
    print "Found entry for %s: %s" % (name, whitebook[name])

else:
    print "Entry not found."

#Sets an entry
if menu_number == "2":
    print "Please add the name and number to create a new entry:"
    add_entry_name = raw_input("Name: ")
    add_entry_phone = raw_input("Phone Number: ")
    whitebook[add_entry_name] = add_entry_phone
    print "Entry stored for %s" % add_entry_name
else:
    print "Failure to store entry."

#Deletes an entry
if menu_number == "3":
    print "Please enter a name to delete from the phonebook."
    delete_entry = raw_input("Name: ")
    del whitebook[delete_entry]
    print "Deleted entry for %s" % delete_entry
else:
    print "Contact not found."

#Lists all entries
if menu_number == "4":
    print "All entries in the phonebook:"
    entries = whitebook.items()
    print entries
else:
    pass

#Saves all entries
if menu_number == "5":
    # open the file in write mode (w)
    whitebook = open('phonebook.pickle', 'w')
    # dump the contents of the phonebook_dict into myfile - the open file
    pickle.dump(whitebook_dict, whitebook)
    # close myfile
    whitebook.close()
    print "All entries saved to the phonebook."

else:
    print "Entries failed to save."

#Quits program
if menu_number == "6":
    print "Goodbye!"
    raise SystemExit
else:
    "Invalid option."
