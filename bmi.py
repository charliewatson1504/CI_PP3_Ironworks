"""
bmi.py is used to hold the class for creating an instance of Person.
"""


# pylint doesn't like that the class has 1 method.
# A future method would be to update the stored data with the bmi score.
# This isn't possible at this time to do so.
class Person:  # pylint: disable=too-few-public-methods
    """
    Creates an instance of Person

    @param weight(float): one of the values needed to calculate bmi
    @param height(float): one of the values needed to calculate bmi
    """

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calc_bmi(self):
        """
        calc_bmi takes the weight and height of the person and
        calculates their bmi
        """
        # Calculates bmi from params
        bmi = self.weight/((self.height/100)*(self.height/100))

        # Rounds calculation to 2 decimal points
        rounded_bmi = round(bmi, 2)
        return rounded_bmi
