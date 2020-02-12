# -*- coding: utf-8 -*-

## Revision history (2020-02-12)
# Created the following functions:
#1) open_external_file; 2) user_binary_symbol_on; 3)
# replace_text_simple; 4) replace_text_negative
# Added these changes:
# updated existing functions to take the variable containing user's 'on' value
# updated the functions to use the imported text file instead of the
hard coded binary icon


def create_icon_grid():
    '''Creates a grid with hardcoded values for the content of the icon.

    This static function defines variables with entries of 1 and 0 for
each of the
    ten lines in the icon grid. 1s represent shaded cells and 0s represent empty
    cells. The individual lines are then packed into an icon_grid
list. This list
    is returned by the function for use elsewhere. This function could
be altered
    with hardcoded grid values for other printable icons.
    '''
    line_1 = [0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
    line_2 = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
    line_3 = [1, 1, 1, 0, 0, 1, 0, 1, 0, 0]
    line_4 = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    line_5 = [1, 1, 1, 0, 0, 0, 0, 1, 0, 0]
    line_6 = [0, 0, 0, 1, 1, 1, 0, 1, 0, 0]
    line_7 = [0, 0, 0, 0, 0, 1, 0, 1, 0, 0]
    line_8 = [0, 0, 0, 0, 0, 1, 0, 1, 0, 0]
    line_9 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    line_10 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    icon_grid = [
        line_1,
        line_2,
        line_3,
        line_4,
        line_5,
        line_6,
        line_7,
        line_8,
        line_9,
        line_10
        ]
    return icon_grid

def open_external_file():
    """
    This function will take in a plaintext file of non-separated
values in a single string inside a list.

    """
    with open('binary.txt') as file:
        read_the_file = file.read()
        list_of_bytes = []
        list_of_bytes.append(read_the_file)
    return list_of_bytes

def user_binary_symbol_on():
    """
    This function is intended to prompt a user to enter the value they
have selected to be their "on" value
    in their binary code. It can be any value provided it only
contains a length value of one.
    """
    user_choice_on = ""
    max_length = '1'
    while user_choice_on == "":
        user_choice_on = input("\nPlease enter the single value which
indicates 'on' (such as '1'): ")
        if len(user_choice_on) > len(max_length):
            print("\nYou can only enter one value. Please try again.")
            user_choice_on = ""
    return user_choice_on


def replace_text_simple(cells, user_pick):
    """
    Takes the iterated list values and replaces the binary with the
desired image characters.
    If the list element is equal to the user's on value the function
prints an "at" symbol and a whitespace.
    Otherwise the function prints a whitespace separated by another whitespace.
    """
    if cells == user_pick:
        print("@", end=" ")
    else:
        print(" ", end=" ")


def replace_text_negative(cellz, uzer_pick):
    """
    This is the negative inversion of the replace_test_simple
function. This function prints
    a whitespace (followed by another whitespace) where it encounters
the user's on value and prints
    an "at" symbol separated by a whitespace otherwise.
    """
    if cellz == uzer_pick:
        print(" ", end=" ")
    else:
        print("@", end=" ")


def simple_print(user_value):
    '''Prints the simplest version of the icon.

    It loops over the icon_grid, unpacking the full list of lists. It then
    unpacks each individual list, checks if each list item is a 1 or 0, then
    prints the appropriate character for each value. It uses space separators
    and return characters to space the output text in a pleasing manner.
    '''
    icon_grid = open_external_file()
    for line in icon_grid:
        for cell in line:
            replace_text_simple(cell, user_value)
        print("\r")

def mirror_print(user_value):
    '''Prints a mirror image version of the icon.

    This function is very similar to the simple_print() function. It loops
    over the icon_grid, unpacking the full list of lists. It then uses reverse()
    to reverse each list in place. After reversing a list, it loops over it,
    checking if each list item is a 1 or 0, then prints the
appropriate character
    for each value. It uses space separators and return characters to space the
    output text in a pleasing manner.
    '''
    icon_grid = create_icon_grid()
    for line in icon_grid:
        line.reverse()
        for cell in line:
            replace_text_negative(cell, user_value)
        print("\r")

def negative_print(user_value):
    '''Prints a photo negative version of the icon.

    This is very similar to simple_print(), but reverses the printed characters.
    It loops over the icon_grid, unpacking the full list of lists. It
then unpacks
    each individual list, checks if each list item is a 1 or 0, then prints the
    "negative" character for each value. It uses space separators and return
    characters to space the output text in a pleasing manner.
    '''
    icon_grid = create_icon_grid()
    for line in icon_grid:
        for cell in line:
            replace_text_negative(cell, user_value)
        print("\r")

def icon_menu():
    '''A menu that lets the user choose which icon version to print.

    This function displays a menu to the user that lets them choose how they'd
    like to see the icon printed. It validates their input and then
returns it as
    a variable for use elsewhere.
    '''
    user_choice = ""
    while user_choice == "":
        user_choice = input(
        "\nPlease select which version of the lovely swimming goose icon " +
        "you'd like to see." +
        '''
            1. Default version
            2. Mirrored version
            3. Photo negative version
            ''')
        if user_choice not in ["1", "2", "3"]:
            print("\nThat's not a valid menu option!\n\n")
            user_choice = ""
    return user_choice

def icon_printer(user_choice, binary_value):
    '''Prints the user's chosen icon.

    This function takes the user_choice variable from the icon_menu() function
    and calls the relevant print function for the choice they made.
    '''
    if user_choice == "1":
        simple_print(binary_value)
    if user_choice == "2":
        mirror_print(binary_value)
    if user_choice == "3":
        negative_print(binary_value)

def main():
    from_a_file = open_external_file()
    full_value = user_binary_symbol_on()
    user_choice = icon_menu()
    icon_printer(user_choice, full_value)

if __name__ == "__main__":
    main()
