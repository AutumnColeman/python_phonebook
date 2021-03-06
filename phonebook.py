#You will write a command line program to manage a phone book. When you start the phonebook.py program, it will print out a menu and ask the user to enter a choice:
#If they choose to look up an entry, you will ask them for the person's name, and then look up the person's phone number by the given name and print it to the screen.
#If they choose to set an entry, you will prompt them for the person's name and the person's phone number,
#If they choose to delete an entry, you will prompt them for the person's name and delete the given person's entry.
#If they choose to list all entries, you will go through all entries in the dictionary and print each out to the terminal.
#If they choose to quit, end the program.
import pickle
from os.path import exists

filename = "phonebook2.pickle"

if exists('phonebook.pickle'):
    print "Loading phonebook"
    phonebook_file = open("phonebook.pickle", "r")
    phonebook_dict = pickle.load(phonebook_file)
    phonebook_file.close()

else:
    phonebook_dict = {}

while True:
    #Looks up an entry
    def look_up():
        name = raw_input("Name? ")
        if name in phonebook_dict:
            info_dict = phonebook_dict[name]
            print "Found entry for %s: " % (name)
            print "Cell Phone Number: %s" % (info_dict["Cell"])
            print "Home Phone Number: %s" % (info_dict["Home"])
            print "Work Phone Number: %s" % (info_dict["Work"])

        else:
            print "Entry for %s not found." % name

    #Sets an entry
    def set_entry():
        print "Please add the name and number to create a new entry:"
        name = raw_input("Name: ").strip()
        cell_phone = raw_input("Cell Phone Number? ")
        home_phone = raw_input("Home Phone Number? ")
        work_phone = raw_input("Work Phone Number? ")
        info_dict = {
            "Cell": cell_phone,
            "Home": home_phone,
            "Work": work_phone}
        phonebook_dict[name] = info_dict
        print "Entry stored for %s" % name


    #Deletes an entry
    def delete_entry():
        print "Please enter a name to delete from the phonebook."
        name = raw_input("Name: ").lower()
        if name in phonebook_dict:
            del phonebook_dict[name]
            print "Deleted entry for %s" % name
        else:
            print "%s not found." % name

    #Lists all entries
    def list_entries():
        for name, info_dict in phonebook_dict.items():
            print "Found entry for %s: " % (name)
            print "*" * 30
            print "Cell Phone Number: %s" % (info_dict["Cell"])
            print "Home Phone Number: %s" % (info_dict["Home"])
            print "Work Phone Number: %s" % (info_dict["Work"])
            print "*" * 30


    #Saves all entries
    def save_entries():
        phonebook_file = open("phonebook.pickle", "w")
        pickle.dump(phonebook_dict, phonebook_file)
        phonebook_file.close()
        print "Entries saved to the phonebook."


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

    menu_number = int(raw_input("What do you want to do (1-6)? "))

    if menu_number == 1:
        look_up()
    elif menu_number == 2:
        set_entry()
    elif menu_number == 3:
        delete_entry()
    elif menu_number == 4:
        list_entries()
    elif menu_number == 5:
        save_entries()
    elif menu_number == 6:
        print "Goodbye!"
        break
    elif menu_number > 6:
        print "Invalid option. Please enter a valid option (1-6)."
