#1 Create two variables - one with your name nd one with your age
#2 Create a function which prints out your data as one string
#3 Create a funtion which prints ANY data (two arhuments) as one string
#4 Create a function which calculates and returns the number of decades you are alive

name = input('What is your name: ')
age = input('What age are you: ')


def name_and_age():
    return  (name + " " + age)


def two_arguments(a, b):
    return (a + b)


def number_of_decades():
    decades = int(age) / 10
    return decades

d = name_and_age()
print(d)

e = two_arguments("12", "13")
print(e)

f = number_of_decades()
print(int(f))



# Below is the solution from the tutor

#1 Create two variables - one with your name nd one with your age
user_name = input('Enter your name: ')
user_age = input('Enter your age too: ')

#2 Create a function which prints out your data as one string
def print_user_data():
    """ Prints the user name (uses global variables)"""
    print(user_name + ' ' + user_age )

print_user_data()

#3 Create a funtion which prints ANY data (two arhuments) as one string
def print_concatenated_data(el1, el2):
    """ Print two concatenated strings.
    
    Arguments:
        :param el1: The first string to be concatenated.
        :param el2: The second string to be concatenated."""
    print(el1 + ' ' + el2)

print_concatenated_data(user_name, user_age)

#4 Create a function which calculates and returns the number of decades you are alive
def calculate_decades(age):
    """ Calculates the integer part of the age received
    
    Arguments:
        :param age: The age for which the decades should be calculated.

    Returns the decades lived.
    """
    decades_lived = age // 10
    return decades_lived


decades = calculate_decades(int(user_age))
print(decades)

