import pickle
import os.path


def init():
    if os.path.exists("newPhonebook.pickle"):
        with open("newPhonebook.pickle", 'rb') as fh:
            phonebook = pickle.load(fh)
    else:
        phonebook = {}
        save(phonebook)
        #create phonebook, create pickle file
    print("\n\n\n\n\nWelcome to your Phonebook! ")
    return phonebook

def main():
    input("Press ENTER to continue >> ")
    print("""
    Electronic Phone Book
    =====================

    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit\n
    What do you want to do (1-5)?
    """)
    choice = input(">> ")

    if choice in choices:
        choices[choice]()
    else:
        print("I'm sorry, you'll have to choose 1-5.")
        main()

def lookup():
    toFind = input("Whose number would you like to look up? >> ")
    if toFind not in phonebook:
        print(f"{toFind} not currently in Phonebook!")
    else:
        num = phonebook[toFind]
        print(f"{toFind}: {num}")
    main()

def addNum():
    newName = input("Please enter a new name. >> ")
    newNum = input(f"Please enter {newName}'s number. >> ")
    phonebook[newName] = newNum
    print(f"NEW ENTRY -- {newName}: {newNum}")
    main()

def delNum():
    killName = input("Please enter the name to delete. >> ")
    if killName not in phonebook:
        print(f"{killName} not currently in Phonebook!")
    else:
        confirm = input(f"Are you sure you want to delete {killName}? Y/N >> ")
        if confirm.lower() == "y":
            del phonebook[killName]
        print(f"{killName} deleted from Phonebook.")
    main()

def listAll():
    if phonebook == {}:
        print("No phone numbers yet!")
    for key, value in phonebook.items():
        print(f"{key}: {value}")
    print("\n")
    main()

def quitting():
    print("Goodbye!\n")
    save(phonebook)

def save(dict):
    # saves the current phonebook to pickle file
    with open("newPhonebook.pickle", 'wb') as fh:
        pickle.dump(dict, fh)
    pass

choices = {
    "1": lookup,
    "2": addNum,
    "3": delNum,
    "4": listAll,
    "5": quitting
}




phonebook = init()

main()


