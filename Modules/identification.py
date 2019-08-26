# This file exports globals variables to be imported when a reference needs to
# be made to the user. Maybe not the best solution, but for now this does the trick.
username = 'zhack'
age = 19
gender = 'male'


def return_username():
    global username


def return_age():
    global age


def return_gender():
    global gender