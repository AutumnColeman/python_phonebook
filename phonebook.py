#You will write a command line program to manage a phone book. When you start the phonebook.py program, it will print out a menu and ask the user to enter a choice:
#If they choose to look up an entry, you will ask them for the person's name, and then look up the person's phone number by the given name and print it to the screen.
#If they choose to set an entry, you will prompt them for the person's name and the person's phone number,
#If they choose to delete an entry, you will prompt them for the person's name and delete the given person's entry.
#If they choose to list all entries, you will go through all entries in the dictionary and print each out to the terminal.
#If they choose to quit, end the program.
whitebook = {
    "Autumn": "770-555-5555",
    "Bob": "404-555-5555",
    "Cat": "678-555-5555",
    "Dog": "470-555-5555"
}

print """
Electronic Phone Book
=====================

1\. Look up an entry
2\. Set an entry
3\. Delete an entry
4\. List all entries
5\. Quit
"""
menu_number = raw_input("What do you want to do (1-5)? ")

if menu_number == 1:
    name = raw_input("Name? ")
    whitebook.get(name, "There is no entry under that name.")
