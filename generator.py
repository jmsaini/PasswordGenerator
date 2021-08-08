import random
import string


def check_input():
    """
    Checks whether the user input is an integer and whether it is equal to 8 or
    greater than 8
    """
    user_input = input("Enter the desired length of the password: ")
    try:
        int(user_input)
        generate_password(int(user_input))
    except ValueError:
        print("Please enter a whole number!")
        check_input()
    else:
        if int(user_input) < 8:
            print("The password must have at least 8 characters."
                  + "\n" + "Please enter again!")
            check_input()


def generate_password(user_input: int):
    """
    :return: a random password that satisfies the following requirements
    - at least 8 characters
    - one or more uppercase letters
    - one or more lowercase letters
    - one or more special characters
    """
    length = user_input

    password = ""

    while len(password) < length:

        one_num = random.randint(1, 9)
        special_char = random.choice(string.punctuation)
        lowercase = string.ascii_lowercase
        one_lowercase = random.choice(lowercase)
        uppercase = string.ascii_uppercase
        one_uppercase = random.choice(uppercase)
        password += str(one_num) + special_char + one_lowercase + one_uppercase
        password = ''.join(random.sample(password, len(password)))

    print("Your password is: " + password[:length])


if __name__ == '__main__':
    check_input()

