#PrettyTable for contacts in terminal
#Json for storing data
#Pathlib for reading and writing into the json file easier
from prettytable import PrettyTable
import json
from pathlib import Path

#creating the cTtable(contact table)
cTable = PrettyTable(['Name', 'Phone Number', 'Email'])
#contacts variable
contacts = []

#storage

#user action functions
#add contact
def addContact():
    print('addContact')

#remove contact
def removeContact():
    print('removeContact')

#search
def search():
    print('search')

#show full list
def show():
    print('show')

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
            show()
        case 2:
            search()
        case 3:
            addContact()
        case 4:
            removeContact()
        case 5:
            break
        case _:
            print('Invalid input')
            continue