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

users = SHEET.worksheet('users')

data = users.get_all_values()

print(data)