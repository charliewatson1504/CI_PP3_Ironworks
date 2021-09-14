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
    user_data = USERS.get_all_values()
    usernames = user_data[0]
    account_types = user_data[1]
    user_dict = {}
    for username in usernames:
        for account_type in account_types:
            user_dict[username] = account_type
            account_types.remove(account_type)
            break
    return user_dict
