"""
parq.py is responsible to handling the PARQ from that is to be
completed by the user when they create a new account
"""

# tuple used for conditions so that the list cannot be changed
CONDITIONS = (
    'Covid symptoms', 'Have cold or flu', 'Have any aches or pains',
    'Are you pregnant', 'Wear glasses/contact lenses', 'None of the above'
    )


def parq_form():
    """
    parq function asks the user some questions of their medical
    history and takes their input. With the inputs they are
    appended to the parq google worksheet
    """

    print('\nThanks for creating an account with Ironworks')
    print('Before you can book a session with one of our')
    print('trainers we need you to complete our PARQ form.')
    print('This is just to take some basic medical information')
    print('so that our trainers can act with the duty of care owed.')

    print('/nAfter each question please enter your answer and press enter')
    full_name = input('\nFull name:')
    email = input('\nEmail address:')
    print('\nDo you have any Injuries or medical conditions')
    med_cond = input('\nEnter details here:')
    print('\nDo you have any of the below:')
    for cond in CONDITIONS:
        print(cond)
    other_cond = input('\nEnter details here:')

    parq_answers = [full_name, email, med_cond, other_cond]
    return parq_answers


parq_form()
