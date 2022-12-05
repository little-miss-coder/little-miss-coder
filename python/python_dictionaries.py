#This program was made to practice with dictionaries and key:value pairs
#It has a "menu" where each number will run a corresponding function.


#make dictionary global so any function can use it
addressBook = {'Maria':'mariag@lakeland.edu', 'Cristi':'cristi123@gmail.com'}

def main():
    
    #call menu function to get action number
    action = menu()
    while action != 6:
        if action == 1:
            lookUp()
        elif action == 2:
            addEntry()
        elif action == 3:
            changeEntry()
        elif action == 4:
            deleteEntry()
        elif action == 5:
            showPhonebook()

        #keep calling menu until user chooses 6 (Quit)
        action = menu()


    print('Thanks for using my program! Bye!')


def menu():

    print()
    print('***Menu***')
    print('1: Look up an email address.')
    print('2: Add a new name and email address.') 
    print('3: Change an existing email address.')
    print('4: Delete an existing name and email address.')
    print('5: View current phonebook.')
    print('6: Quit.')
    print()

    action = int(input('Enter the number for the action you would like to do: '))

    #validate that they entered a valid selection
    while action < 1 or action > 5:
        action = int(input('Invalid action number. Enter the number for the action you would like to do: '))
        

    return action

def lookUp():
    lookup_item = input('Enter the name you want to look up: ')

    #if name is not found it will return "Email not found" as the value
    value = addressBook.get(lookup_item, 'Email not found.')
    
    print(f'User: {lookup_item}')
    print(f'Email: {value}')
    print()

    
def addEntry():
    name = input('Enter the name you would like to add: ')
    email = input(f"Enter {name}'s email: ")


    global addressBook #call global, needed in order to make changes
    
    addressBook[name] = email

    print('Name and email added to address book.')
    print()

def changeEntry():
    name = input('Enter the name you want to change the email for: ')

    global addressBook #call global to make changes
    
    if name in addressBook:
        email = input(f'Enter the new email address for {name}: ')
        addressBook[name] = email
    else:
        print(f'Sorry, {name} was not found in the address book.')

def deleteEntry():
    name = input('Enter the name for the entry you would like to delete: ')
    global addressBook
    
    if name in addressBook:
        del addressBook[name]
        print(f'{name} deleted.')
    else:
        print(f'Sorry, {name} was not found.')

def showPhonebook():
    print(f'{"Name:":<20}{"Email:":>31}')
    #prints all values in address book.
    for key in addressBook:
        print(f'{key:<20} {addressBook[key]:>30}')
    

if __name__ == '__main__':
    main()


'''
OUTPUT:

***Menu***
1: Look up an email address.
2: Add a new name and email address.
3: Change an existing email address.
4: Delete an existing name and email address.
5: Quit.

Enter the number for the action you would like to do: 4
Enter the name for the entry you would like to delete: Maria
Maria deleted.
***Menu***
1: Look up an email address.
2: Add a new name and email address.
3: Change an existing email address.
4: Delete an existing name and email address.
5: Quit.

Enter the number for the action you would like to do: 1
Enter the name you want to look up: Maria
User: Maria
Email: Email not found.

***Menu***
1: Look up an email address.
2: Add a new name and email address.
3: Change an existing email address.
4: Delete an existing name and email address.
5: Quit.

Enter the number for the action you would like to do: 2
Enter the name you would like to add: Maria
Enter Maria's email: mgilipsky@gmail.com
Name and email added to address book.

***Menu***
1: Look up an email address.
2: Add a new name and email address.
3: Change an existing email address.
4: Delete an existing name and email address.
5: Quit.

Enter the number for the action you would like to do: 5
Thanks for using my program! Bye!
'''
