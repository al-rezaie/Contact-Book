#PrettyTable for contacts in terminal
#Json for storing data
#Pathlib for reading and writing into the json file easier
from prettytable import PrettyTable
import json
from pathlib import Path

#creating the cTtable(contact table)
cTable = PrettyTable(['Name', 'Phone Number', 'Email'])
#contacts variable
contacts = [
    {
        'name': 'mmd',
        'phoneNumber': '12345678901',
        'email': 'mmd@gmail.com'
    },
    {
        'name': 'esi',
        'phoneNumber': '11111111111',
        'email': 'esi@gmail.com'
    },
    {
        'name': 'sari',
        'phoneNumber': '33333333333',
        'email': 'sari@gmail.com'
    },
]

#storage

#user action functions
#add contact
def addContact():
    name = input('Name: ')
    phoneNumber = input('Phone Number: ')
    email = input('Email: ')
    
    newContact = {
            'name':name,
            'phoneNumber':phoneNumber,
            'email':email
        }
    contacts.append(newContact)

#remove contact
def removeContact():
    #name of the contact that needs to be deleted
    toDelete = input('Name, Email, or Phone Number: ')
    #finding the index of the contact
    index = search(toDelete)
    #checking to see if there was anyone found
    if type(index) is int:
        contacts.pop(index)
        return 'contact deleted successfully'
    else:
        return index

#search
def search(value):
    try:
        int(value)
        mode = 'phoneNumber'
    except:
        if '@' in value:
            mode = 'email'
        else:
            mode = 'name'
        
    for i, dic in enumerate(contacts):
        if dic[mode] == value:
            return i
    return '\nNo contact were found'

#show full list
def show(items):
    cTable.clear_rows()
    if type(items) == list:
        for _, dic in enumerate(items):
            cTable.add_row([dic['name'], dic['phoneNumber'], dic['email']])
    else:
        cTable.add_row([items['name'], items['phoneNumber'], items['email']])
            
    print(cTable)

while True:
    #initializing the program
    print('''
        1.Show the list of contacts
        2.Search
        3.Add contact
        4.Remove contact
        5.Exit
        ''')
    #get the user choice
    chosenAction = int(input())
    #check the user choice using match
    match chosenAction:
        case 1:
            show(contacts)
        case 2:
            toSearch = input('Name, Email, or Phone Number: ')
            index = search(toSearch)
            if type(index) is int:
                contact = contacts[index]
                show(contact)
            else:
                print(index)
        case 3:
            addContact()
        case 4:
            print(removeContact())
        case 5:
            break
        case _:
            print('Invalid input')
            continue