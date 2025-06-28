#PrettyTable for contacts in terminal
#Json for storing data
#Pathlib for reading and writing into the json file easier
#RE(regex, regular expression) for validating user input
from prettytable import PrettyTable
import json
from pathlib import Path
import re

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
    try:
        name = input('Name: ')
        phoneNumber = input('Phone Number: ')
        #regex meaning -> must start with 09 have at lease 11 chars (9 chars after 09) all digits
        valPhoneNumber = re.findall('^09\d{9}$', phoneNumber)
        if not valPhoneNumber:
            return '\nPhone Number format is incorrect. 09xxxxxxxxx all digits.'
        email = input('Email: ')
        #regex meaning -> start with number, upper, or lower case letters
                        # 63 other chars with upper, lower, number (totally 64 char)
                        # an @
                        # upper, lower, number after @
                        # upper, lower, number, ., - with no count validation
                        # a .
                        # upper or lower
                        # end with at least 2 chars (for domain (.com, .io, ...))
        valEmail = re.findall('^[a-zA-Z0-9][a-zA-Z0-9._%+-]{0,63}@[a-zA-Z0-9][a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        if not valEmail:
            return '\nEmail format is incorrect. xxx@xxx.com the length is not important.'
        
        newContact = {
                'name':name,
                'phoneNumber':phoneNumber,
                'email':email
            }
        contacts.append(newContact)
        return '\nContact was added successfully'
    except:
        return '\nSomthing went wrong'

#remove contact
def removeContact():
    try:
        #name of the contact that needs to be deleted
        toDelete = input('Name, Email, or Phone Number: ')
        #finding the index of the contact
        index = search(toDelete)
        #checking to see if there was anyone found
        if type(index) is int:
            contacts.pop(index)
            return '\nContact deleted successfully'
        else:
            return index
    except:
        return '\nSomthing went wrong'

#search
def search(value):
    try:
        #check to see which property to search with:
        #value is int: phone number
        try:
            int(value)
            mode = 'phoneNumber'
        except:
            #value contains @ with email
            if '@' in value:
                mode = 'email'
            #none of them with name
            else:
                mode = 'name'
        #using the enumerate function to search in the list of contact(dictionaries)
        for i, dic in enumerate(contacts):
            #using the mode variable to select the key we're searching on
            if dic[mode] == value:
                #return the index if there was a match
                return i
            #return an error if there was no match
        return '\nNo contact were found'
    except:
        print('\nSomething went wrong')

#show full list
def show(items):
    try:
        #clear the rows so there are no rows that dosen't match our needs
        cTable.clear_rows()
        #if the argument was list we need to show all the contacts so we loop on it
        if type(items) == list:
            #since we doesn't need the index ulike the search function we use _ as a place holder rather than declaring a variable
            for _, dic in enumerate(items):
                cTable.add_row([dic['name'], dic['phoneNumber'], dic['email']])
        #if the argument was not a list, it's a dictionary(check the search section) so we just use the keys to create a row
        else:
            cTable.add_row([items['name'], items['phoneNumber'], items['email']])
                
        print(cTable)
    except:
        print('\nSomething went wrong')

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
            #finding the index of toSearch using search function
            index = search(toSearch)
            #if it was int it means the search function has found something
            if type(index) is int:
                #we use the index that we receive from the search function to choose the contact
                contact = contacts[index]
                #we give the contact(dictionary) to the show function in order to print it
                show(contact)
            #if it was not int it means the search function has not found anything and we print the error message
            else:
                print(index)
        case 3:
            print(addContact())
        case 4:
            print(removeContact())
        case 5:
            break
        case _:
            print('Invalid input')
            continue