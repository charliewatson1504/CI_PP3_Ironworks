"""
google_sheet is used to handle the getting and updating of the data on the
ironworks google sheet.

gspread is used to send and recieve the data to a google spreadsheet

Credentials from google.oauth2.service_account give the access to the data
"""

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

"""
Credit to Code Institue Love Sandwiches mock project for giving the run
through on how to do this.

SCOPE, CREDS, SCOPED_CREDS, GSPREAD_CLIENT and SHEET allow us to gain
access to the sheet and get data and update.
"""

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ironworks')

"""
USERS, STEVE, KAREN allow us to access the speific worksheets within the
google sheet.
"""

USERS = SHEET.worksheet('users')
STEVE = SHEET.worksheet('steve')
KAREN = SHEET.worksheet('karen')


def get_usernames():
    """
    get_usernames first gets all values from the users google worksheet.
    With that data it combines the 2 lists into a dictionary with the username
    as the key and the account type as the value.
    """
    usernames = USERS.col_values(1)
    account_types = USERS.col_values(2)
    user_dict = {}
    for username in usernames:
        for account_type in account_types:
            user_dict[username] = account_type
            account_types.remove(account_type)
            break
    return user_dict


def get_staff_data(staff):
    """
    get_staff takes 1 parameter of staff and puts the data into a dictionary.
    This is so that it can be used for any staff member even if the
    amount of staff numbers increases. As the data is stored the same
    way on each worksheet it can be handled the same way to prevent
    repeating code.
    """
    dates = staff.col_values(1)
    booking_status = staff.col_values(2)
    staff_dict = {}
    for date in dates:
        for status in booking_status:
            staff_dict[date] = status
            booking_status.remove(status)
            break
    return staff_dict
