import re


def get_name():
    x = input('Enter your name:')
    while not re.search(r"^[A-Z][a-z]+$", x):
        print("Name should start with uppercase character and contain only letters.")
        x = input('Enter your name:')
    return x


def get_surname():
    x = input('Enter your surname:')
    while not re.search(r"^[A-Z][a-z]+$", x):
        print("Surname should start with uppercase character and contain only letters.")
        x = input('Enter your surname:')
    return x


def get_city():
    x = input('Enter your city:')
    while not re.search(r"^[A-Z][a-z]+$", x):
        print("City name should start with uppercase character and contain only letters.")
        x = input('Enter your city:')
    return x


def get_phone():
    x = input('Enter your phone number:')
    while not re.search(r"^[(][0-9]{2}[)][0-9]{3}-[0-9]{2}-[0-9]{2}$", x):
        print("Phone number should have format (61) 222-45-56.")
        x = input('Enter your phone number:')
    return x


def get_postcode():
    x = input('Enter your post code:')
    while not re.search(r"^[0-9]{2}-[0-9]{3}$", x):
        print("Post code should have format 11-111.")
        x = input('Enter your post code:')
    return x


def person_data():
    name = get_name()
    surname = get_surname()
    city = get_city()
    phone = get_phone()
    post_code = get_postcode()


person_data()