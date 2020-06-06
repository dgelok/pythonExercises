
import pickle

# with open('phonebook.pickle', 'rb') as fh:
#     phonebook = pickle.load(fh)
#     print(phonebook)

phonebook = {
    'dan gelok': '832-266-7763',
    'emergency': '911',
    'singapore fire line': '995'
}

menuscreen = """
Electronic Phone Book
=====================

    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit\n
    What do you want to do (1-5)?
"""

def lookupEntry():
    name = input("What is the name you would like to look up? >> ")
    name = name.lower()
    if name not in phonebook:
        print("I'm sorry, I do not have that name registered.")
    else:
        number = phonebook[name]
        print(f"The number for {name} is {number}.")

def setEntry():
    newname = input("What is the new name to add? >> ")
    newnum = input(f"What is {newname}'s number? >> ")
    phonebook[newname] = newnum

def deleteEntry():
    nameToDelete = input("Which name would you like to delete? >> ")
    confirm = input(f"Are you sure you want to delete {nameToDelete}? Y/N >> ")
    confirm = confirm.lower()
    if confirm == "y":
        print(f"Deleting {nameToDelete}...")
        if nameToDelete not in phonebook:
            print("I'm sorry, I have no record of that name.")
        else:
            del phonebook[nameToDelete]

def listEntries():
    print("You have the following entries:\n")
    for key, value in phonebook.items():
        print(f"{key}: {value}")

while True:
    print(menuscreen)
    choice = input(">> ")
    if choice == "1":
        # look up an entry
        lookupEntry()
    elif choice == "2":
        # set entry
        setEntry()
    elif choice == "3":
        # delete entry
        deleteEntry()
    elif choice == "4":
        # list entries
        listEntries()
    elif choice == "5":
        break
    else:
        print("Sorry, please type a number, 1-5.")
    input("Please hit ENTER to continue. >> ")





# info that does file I/0

print("\n\tGoodbye!\n")

with open('phonebook.pickle', 'wb') as fh:
    pickle.dump(phonebook, fh)