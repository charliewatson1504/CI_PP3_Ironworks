"""
This is the main py file for Ironworks Personal Training Booking System.
The main purpose is to allow users to book sessions and staff to see
which sessions they have booked and with who.
All data required to be stored is done so on a google spreadsheet.
"""

import google_sheet

def welcome_screen():
    """
    Welcome message to the user along with an option to login or create an account
    """
    while True:
        print('Please enter l to login using your username or c to create an account')

        answer = input('Enter your choice here:\n')

        # validate_login(answer)

        # if validate_login(answer):

        if answer == 'l':
            login()
            break
        else:
            create_account()
            break

# def validate_login(data):
#     try:

def login():
    print('You have logged in')

def create_account():
    print('Please create a new account')

print('Welcome to the Ironworks Personal Training Booking System\n')
welcome_screen()