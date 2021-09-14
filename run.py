"""
This is the main py file for Ironworks Personal Training Booking System.
The main purpose is to allow users to book sessions and staff to see
which sessions they have booked and with who.
All data required to be stored is done so on a google spreadsheet.
"""

import google_sheet as gs


def welcome_screen():
    """
    Welcome message to the user along with an option to login or create an
    account
    """
    while True:
        print('Welcome to the Ironworks Personal Training Booking System\n')
        print('After typing your choice please press enter button\n')
        print('Please enter l to login using your username')
        print('or c to create an account')

        answer = input('Enter your choice here:')
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
    """
    login function first takes an username from the user and then
    checks that against the usernames stored in the google worksheet.
    """
    while True:
        answer = input('Enter your username and press enter:')
        answer = answer.lower()
        usernames = gs.get_usernames().keys()
        if answer in usernames:
            print('username found')
            return False
        else:
            print(f'\n{answer} is not a valid username.')
            print('would you like to create an account?')
            print('Enter y for Yes and n for No')
            new_answer = input('Enter choice here:')
            if new_answer == 'y':
                create_account()
                return False
            else:
                print('Taking you back to the welcome screen....\n')
                welcome_screen()
                return False


def create_account():
    print('Please create a new account')



welcome_screen()
