"""
This is the main py file for Ironworks Personal Training Booking System.
The main purpose is to allow users to book sessions and staff to see
which sessions they have booked and with who.
All data required to be stored is done so on a google spreadsheet.
"""

import google_sheet


def welcome_screen():
    """
    Welcome message to the user along with an option to login or create an
    account
    """
    while True:
        print('Please enter l to login using your username')
        print('or c to create an account')

        answer = input('Enter your choice here:\n')
        answer = answer.lower()

        if answer == 'l':
            print('Valid choice. Loading login.....')
            login()
            return False
        
        if answer == 'c':
            print('Valid choice. Loading create account.....')
            create_account()
            return False
        
        print(f'{answer} is an invalid entry, please use l or c')


def login():
    print('You have logged in')


def create_account():
    print('Please create a new account')


print('Welcome to the Ironworks Personal Training Booking System\n')
welcome_screen()
