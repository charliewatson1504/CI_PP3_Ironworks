"""
users.py allows for creating a class out of the details in the user google worksheet.
This is to assist with validation and determining the type of user account.
Credit to stackoverflow - https://stackoverflow.com/questions/1639174/creating-class-instance-properties-from-a-dictionary
"""


class UserAcc:
    """
    UserAcc class creates objects from a defined dictionary
    and allows access to the values held within the 
    dictionary for data validation.
    """
    username = None
    account = None

    def __init__(self, dictionary):
        self.__dict__.update(dictionary)
