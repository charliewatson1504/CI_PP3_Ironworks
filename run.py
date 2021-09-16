"""
This is the main py file for Ironworks Personal Training Booking System.
The main purpose is to allow users to book sessions and staff to see
which sessions they have booked and with who.
All data required to be stored is done so on a google spreadsheet.
"""

import google_sheet as gs
import bmi as bm
import parq as pq


def welcome_screen():
    """
    Welcome message to the user along with an option to login or create an
    account
    """

    while True:
        print('Welcome to the Ironworks Personal Training Booking System\n')
        print('After typing your choice please press enter button\n')
        print('Please enter l to login')
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

            # Gets usernames from the user google worksheet
            user_dict = gs.get_usernames()

            # Filters user_dict to only entries that have a key
            # of the input given
            # credit to
            # https://realpython.com/iterate-through-dictionary-python/#filtering-items
            new_user_dict = {k: v for k, v in user_dict.items() if k == answer}

            if new_user_dict.get(answer) == 'User':
                print('\nMoving onto user section')

                # If username is a user account takes them to the user section
                user(answer)
                return False

            print('\nStaff section loading...')

            # If username is a staff account takes them to
            # the staff section
            staff(answer)
            return False

        print(f'\n{answer} is not a valid username.')
        print('would you like to create an account?')
        print('Enter y for Yes and n for No')
        new_answer = input('Enter choice here:')

        if new_answer == 'y':

            # Takes user to create a new account
            create_account()
            return False

        print('Taking you back to the welcome screen....\n')

        # Takes user back to the welcome screen
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

            # Adds new username to the users google sheet
            users.append_row(new_user)

            parq_data = pq.parq_form()
            pq.update_worksheet(parq_data)
            after_create_account()
            return False


def after_create_account():
    """
    after create account is called when a user creates a new account
    """

    while True:
        print('\nWhat would you like to do now?')
        print('Enter l to login')
        print('or press e to exit')
        answer = input('\nEnter choice here:')

        # Validates the users input
        if answer == 'l':
            login()
            return False

        if answer == 'e':
            welcome_screen()
            return False

        print('\nInvalid choice entered, please try again')


def validate_username(answer):
    """
    validate_username takes the answer from user and checks if
    username is already in use in google worksheet.
    Created after seeing function needed in multiple uses.
    """

    answer = answer.lower()

    # Gets usernames from the users google sheet
    usernames = gs.get_usernames().keys()

    try:
        if answer in usernames:
            return True

    except ValueError as e:
        print(f'{e} not found')
        return False


def calculate_bmi(name):
    """
    calculate_bmi function uses the Person class from bmi.py.
    Inputs are given by the user which is then used to
    calculate the bmi.
    @param name(str): Username of user
    """
    print('\nWelcome to the bmi calculator')
    print('All that is provided is your bmi score')
    print('We do not provide any interpretation of the score')
    weight = float(input('\nEnter your weight in kilograms:'))
    height = float(input('\nEnter your height in centimeters:'))

    # calling Person class from bmi.py
    bmi = bm.Person(weight, height)

    # using the calc_bmi method from Person class
    calculated_bmi = bmi.calc_bmi()

    print(f'\nYour BMI score is {calculated_bmi}')

    while True:
        print('\nWhat would you like to do now?')
        print('Enter s to view booked sessions')
        print('or b to book a new session')
        print('or e to exit')
        answer = input('\nEnter choice here:')

        if answer == 's':

            # Takes user to view their booked sessions
            booked_sessions(name)
            return False

        elif answer == 'b':

            # Takes user to book a new session
            book(name)
            return False

        elif answer == 'e':

            # Takes user back to the welcome screen
            welcome_screen()
            return False

        else:
            print('Selection is in valid, please try again')


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

            # Takes user to view staff sessions
            staff_sessions(name)
            return False

        elif answer == 'a':

            # Takes user to add an additional session
            # to their schedule
            add_session(name)
            return False

        else:
            print('Selection is in valid, please try again')


def staff_sessions(name):
    """
    staff_sessions takes in 1 parameter from function it is called from. It
    gets the data from the relvant staff google sheet and presents the data
    back to the user.
    @param name(str): Username of staff member
    """

    # Gets data from google sheet for logged in staff member
    staff_data = gs.get_staff_data(name)

    # prints a list of the sessions for that staff member
    for k, v in staff_data.items():
        print("{:<15} {:<10}".format(k, v))

    while True:
        print('\nTo add a new session enter s')
        print('or to go back to welcome screen enter w')
        answer = input('\nEnter choice here:')

        if answer == 's':

            # Takes user to add a session to their schedule
            add_session(name)
            return False

        elif answer == 'w':

            # Takes user back to the welcome screen
            welcome_screen()
            return False

        else:
            print('\nInvalid choice entered, please try again')


def add_session(name):
    """
    add_session takes an input from the user of a date. The input
    is then chceked to make sure it isn't already in use then
    appends the data to the relevant staff worksheet.
    @param name(str): Username of the user
    """

    while True:
        print('\nPlease enter the date of the session you want to add')
        print('Date format to be used is dd-mm-yyyy')
        answer = input('Enter date:')

        # Opens google worksheet of staff member
        staff_sheet = gs.SHEET.worksheet(name)

        # Gets the values from the worksheet of staff member
        staff_data = gs.get_staff_data(name)

        # Checks if date entered is already in google sheet
        if answer in staff_data.keys() is False:
            print(f'\n{answer} is already in use, please chose another')

        else:
            new_date = [answer, 'AVAILABLE']

            # Adds new values to the staffs google worksheet
            staff_sheet.append_row(new_date, value_input_option='USER_ENTERED')
            print(f'\nGreat! {answer} has been added to your schedule\n')
            after_add_session(name)
            return False


def after_add_session(name):
    """
    after add session function is called at the end of adding a new
    session to a staff schedule. Allows the user to navigate through
    the app
    @param name(str): Username of user
    """

    while True:
        print('\nWhat would you like to do now?')
        print('Enter s to view your scheduled sessions')
        print('or press e to exit')
        answer = input('\nEnter choice here:')

        # Validates the users input
        if answer == 's':
            staff_sessions(name)
            return False

        elif answer == 'e':
            welcome_screen()
            return False

        else:
            print('\nInvalid choice entered, please try again')


def user(name):
    """
    user is called when a user logs in. It gives a choice to the user
    on what they would like to do next. It then checks the choice
    is valid.
    @param name(str): Username of user
    """

    while True:
        print(f'Welcome {name} to the Ironworks Booking System')
        print('Enter b to book a session')
        print('or s for booked sessions')
        print('or c for BMI calculation')
        answer = input('\nEnter choice here:')

        # Validates the users entry
        if answer == 'b':

            # Takes user to book a session
            book(name)
            return False

        elif answer == 's':

            # Takes user to view their booked sessions
            booked_sessions(name)
            return False

        elif answer == 'c':

            # Takes user to BMI calculation
            calculate_bmi(name)
            return False

        else:
            print('\nInvalid choice entered, please try again')


def book(name):
    """
    book function allows the user to see available dates for all
    staff members and then go on to book an available session.
    @param name(str): Username of user
    """

    print('\nAvailable dates for Steve\n')

    # Gets values from steve google worksheet
    steve = gs.get_staff_data('steve')

    # Puts values from worksheet into a dictionary and is
    # filtered to entries that have the value of 'AVAILABLE'
    new_steve_dict = {k: v for k, v in steve.items() if v == 'AVAILABLE'}

    # Displays a list of sessions for Steve
    for k, v in new_steve_dict.items():
        print("{:<15} {:<10}".format(k, v))

    print('\nAvailable dates for Karen\n')

    # Gets values from karen google worksheet
    karen = gs.get_staff_data('karen')

    # Puts values from worksheet into a dictionary and is
    # filtered to entries that have the value of 'AVAILABLE'
    new_karen_dict = {k: v for k, v in karen.items() if v == 'AVAILABLE'}

    # Displays a list of sessions for Karen
    for k, v in new_karen_dict.items():
        print("{:<15} {:<10}".format(k, v))

    print('\nWho would you like to book with?')
    print('Enter k for Karen')
    print('or s for Steve')
    trainer = input('\nEnter choice here:')

    # Validates the users input
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

        # Gets values from selected staff google worksheet
        trainer_data = gs.get_staff_data(trainer)

        # Checks to see if date is a valid bookable date
        if date in trainer_data:

            # Puts values into a dictionary filtered on the
            # date the user input
            new_trainer_dict = {
                k: v for k, v in trainer_data.items() if k == date
                }

            for key in new_trainer_dict:
                trainer_dict_value = new_trainer_dict[key]

            # Validates if the selected date is available
            if trainer_dict_value == 'AVAILABLE':

                # Opens the specified google worksheet
                trainer_wks = gs.SHEET.worksheet(trainer)

                # Finds the google sheet cell reference
                # based on the date provided by the user
                row = trainer_wks.find(date).row
                col = trainer_wks.find(date).col

                # Increases the col figure by one so correct
                # column is updated
                new_col = col + 1

                # Updates the specified cell in the google worksheet
                trainer_wks.update_cell(row, new_col, name)

                print(
                    f'\nGreat! {date} has been booked for you with {trainer}'
                    )

                # Takes user to after booking screen
                after_booking(name)
                return False

        else:
            print(f'\n{date} is not available to be booked')
            print('Please try again...\n')


def after_booking(name):
    """
    after_booking function is called when a user has been successful
    in booking a new session.
    @param name(str): Username of user
    """
    while True:
        print('\nWhat would you like to do now?')
        print('Enter s to view your booked sessions')
        print('or press e to exit')
        answer = input('\nEnter choice here:')

        # Validates the users input
        if answer == 's':
            booked_sessions(name)
            return False

        elif answer == 'e':
            welcome_screen()
            return False

        else:
            print('\nInvalid choice entered, please try again')


def booked_sessions(name):
    """
    book_sessions function allows the user to see what sessions they have
    booked with which trainer.
    @param name(str): Username for user
    """

    print('\nBooked sessions with Steve\n')

    # Gets values from steve google worksheet
    steve = gs.get_staff_data('steve')

    # Creates a dictionary from google sheet values and
    # filters them on the specified username
    new_steve_dict = {k: v for k, v in steve.items() if v == name}

    # Displays a list of the sessions user has booked with steve
    for k, v in new_steve_dict.items():
        print("{:<15} {:<10}".format(k, v))

    print('\nBooked sessions with Karen\n')

    # Gets values from steve google worksheet
    karen = gs.get_staff_data('karen')

    # Creates a dictionary from google sheet values and
    # filters them on the specified username
    new_karen_dict = {k: v for k, v in karen.items() if v == name}

    # Displays a list of the sessions user has booked with karen
    for k, v in new_karen_dict.items():
        print("{:<15} {:<10}".format(k, v))

    while True:
        print('\nWhat would you like to do now?')
        print('press b to book another session')
        print('or e to exit')
        answer = input('\nEnter your choice here:')

        # Validates the users input
        if answer == 'b':
            book(name)
            return False

        elif answer == 'e':
            welcome_screen()
            return False

        else:
            print('\nInvalid choice entered, please try again')


welcome_screen()
