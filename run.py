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

        # Checks if username entered exists in google sheet
        if validate_username(answer) is True:
            user_dict = gs.get_usernames()

            # credit to
            # https://realpython.com/iterate-through-dictionary-python/#filtering-items
            new_user_dict = {k: v for k, v in user_dict.items() if k == answer}

            if new_user_dict.get(answer) == 'User':
                print('\nMoving onto user section')
                user(answer)
                return False

            else:
                print('\nStaff section loading...')
                staff(answer)
                return False

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
    """
    create_accout function takes an input from the user for a
    new username, checks it to the list of already used
    usernames and if not used appends it to the users
    google worksheet.
    """

    while True:
        print('\nPlease enter the username you want to use')
        answer = input('Enter username:')

        # checks if the username already exists in google sheet
        if validate_username(answer) is True:
            print(f'\n{answer} is already in use, please chose another')

        else:
            new_user = [answer, 'User']
            users = gs.USERS
            users.append_row(new_user)
            return False


def validate_username(answer):
    """
    validate_username takes the answer from user and checks if
    username is already in use in google worksheet.
    Created after seeing function needed in multiple uses.
    """
    answer = answer.lower()
    usernames = gs.get_usernames().keys()
    if answer in usernames:
        return True
    else:
        return False


def staff(name):
    """
    staff function is to take an input from the user on whether
    they want to view their bookings or add a new session.
    The selection they make will invoke the relevant function
    to take them on in the process.
    @param name(str): Username of staff member
    """
    while True:
        print('\nStaff section')
        print('Enter s to view booked sessions')
        print('or a to add a new session')
        answer = input('\nEnter choice here:')
        print('')

        if answer == 's':
            staff_sessions(name)
            return False

        elif answer == 'a':
            add_session(name)
            return False

        else:
            print('Selection is in valid, please try again')


def staff_sessions(name):
    """
    staff_sessions takes in 1 parameter from function it is called from. It
    gets the data from the relvant staff google sheet and presents the data
    back to the user.
    """
    staff_data = gs.get_staff_data(name)
    for k, v in staff_data.items():
        print("{:<15} {:<10}".format(k, v))
    while True:
        print('\nTo add a new session enter s')
        print('or to go back to welcome screen enter w')
        answer = input('\nEnter choice here:')
        if answer == 's':
            add_session(name)
            return False
        elif answer == 'w':
            welcome_screen()
            return False
        else:
            print('\nInvalid choice entered, please try again')


def add_session(name):
    """
    add_session takes an input from the user of a date. The input
    is then chceked to make sure it isn't already in use then
    appends the data to the relevant staff worksheet.
    """
    while True:
        print('\nPlease enter the date of the session you want to add')
        print('Date format to be used is yyyy')
        answer = input('Enter date:')
        staff_sheet = gs.SHEET.worksheet(name)
        staff_data = gs.get_staff_data(name)
        if answer in staff_data.keys() is False:
            print(f'\n{answer} is already in use, please chose another')
        else:
            new_date = [answer, 'AVAILABLE']
            staff_sheet.append_row(new_date, value_input_option='USER_ENTERED')
            return False


def user(name):
    """
    user is called when a user logs in. It gives a choice to the user
    on what they would like to do next. It then checks the choice
    is valid.
    """
    while True:
        print(f'Welcome {name} to the Ironworks Booking System')
        print('Enter b to book a session')
        print('or s for booked sessions')
        answer = input('\nEnter choice here:')
        if answer == 'b':
            book(name)
            return False
        elif answer == 's':
            booked_sessions(name)
            return False
        else:
            print('\nInvalid choice entered, please try again')


def book(name):
    """
    book function allows the user to see available dates for all
    staff members and then go on to book an available session.
    """
    print('\nAvailable dates for Steve\n')
    steve = gs.get_staff_data('steve')
    new_steve_dict = {k: v for k, v in steve.items() if v == 'AVAILABLE'}
    for k, v in new_steve_dict.items():
        print("{:<15} {:<10}".format(k, v))
    print('\nAvailable dates for Karen\n')
    karen = gs.get_staff_data('karen')
    new_karen_dict = {k: v for k, v in karen.items() if v == 'AVAILABLE'}
    for k, v in new_karen_dict.items():
        print("{:<15} {:<10}".format(k, v))
    print('\nWho would you like to book with?')
    print('Enter k for Karen')
    print('or s for Steve')
    trainer = input('\nEnter choice here:')
    if trainer == 'k':
        trainer = 'karen'
    elif trainer == 's':
        trainer = 'steve'
    else:
        print('\nInvalid choice entered, please try again')
    print(f'{trainer} selected')
    while True:
        print('\nWhat date would you like to book?')
        print('Please use the format dd-mm-yyyy')
        date = input('\nEnter date here:')
        trainer_data = gs.get_staff_data(trainer)
        new_trainer_dict = {
            k: v for k, v in trainer_data.items() if k == date
            }
        print(new_trainer_dict)
        for key in new_trainer_dict:
            trainer_dict_value = new_trainer_dict[key]
        if trainer_dict_value == 'AVAILABLE':
            trainer_wks = gs.SHEET.worksheet(trainer)
            row = trainer_wks.find(date).row
            col = trainer_wks.find(date).col
            new_col = col + 1
            trainer_wks.update_cell(row, new_col, name)
            return False
        else:
            print(f'\n{date} is not available to be booked')
            print('Please try again...\n')


def booked_sessions(name):
    """
    book_sessions function allows the user to see what sessions they have
    booked with which trainer.
    """
    print('\nBooked sessions with Steve\n')
    steve = gs.get_staff_data('steve')
    new_steve_dict = {k: v for k, v in steve.items() if v == name}
    for k, v in new_steve_dict.items():
        print("{:<15} {:<10}".format(k, v))
    print('\nBooked sessions with Karen\n')
    karen = gs.get_staff_data('karen')
    new_karen_dict = {k: v for k, v in karen.items() if v == name}
    for k, v in new_karen_dict.items():
        print("{:<15} {:<10}".format(k, v))


welcome_screen()
