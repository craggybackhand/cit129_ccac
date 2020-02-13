# -*- coding: utf-8 -*-

## Revision history (2020-02-12)
# Created the following functions:
# 1) open_external_file; 2) user_binary_symbol_on; 3)
# replace_text_simple; 4) replace_text_negative
# Added these changes:
# updated existing functions to take the variable containing user's 'on' value
# updated the functions to use the imported text file instead of the
# hard coded binary icon
# Added function to configure the binary file into a grid
# Removed the print_icon function due to input variable restraints and added
# to the main() 
# Edited the open_external_file function to run simpler


def open_external_file():
    """
    This function will take in a plaintext file of non-separated
values in a single string inside a list. This file is hard coded and only editable
within the code itself. To change, simple change the name of the text file in
the parentheses after open() to what your file is called.

    """
    with open('test_file.txt') as file:
        read_the_file = file.read()
    return read_the_file

def configure_file(long_list):
    """
    Take the long string in list form imported from the external file and
    sequence it into ten segments (lines) each ten characters long.
    """
    better_list = []
    long_list = list(long_list)
    better_list.append(long_list[0:10])
    better_list.append(long_list[10:20])
    better_list.append(long_list[20:30])
    better_list.append(long_list[30:40])
    better_list.append(long_list[40:50])
    better_list.append(long_list[50:60])
    better_list.append(long_list[60:70])
    better_list.append(long_list[70:80])
    better_list.append(long_list[80:90])
    better_list.append(long_list[90:100])
    return better_list

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
        user_choice_on = input("\nPlease enter the single value which indicates 'on' (such as '1'): ")
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


def simple_print(icon, user_value):
    '''Prints the simplest version of the icon.

    It loops over the icon_grid, unpacking the full list of lists. It then
    unpacks each individual list, checks if each list item is a 1 or 0, then
    prints the appropriate character for each value. It uses space separators
    and return characters to space the output text in a pleasing manner.
    '''
    icon_grid = icon
    for line in icon_grid:
        for cell in line:
            replace_text_simple(cell, user_value)
        print("\r")

def mirror_print(icon, user_value):
    '''Prints a mirror image version of the icon.

    This function is very similar to the simple_print() function. It loops
    over the icon_grid, unpacking the full list of lists. It then uses reverse()
    to reverse each list in place. After reversing a list, it loops over it,
    checking if each list item is a 1 or 0, then prints the
appropriate character
    for each value. It uses space separators and return characters to space the
    output text in a pleasing manner.
    '''
    icon_grid = icon
    for line in icon_grid:
        line.reverse()
        for cell in line:
            replace_text_negative(cell, user_value)
        print("\r")

def negative_print(icon, user_value):
    '''Prints a photo negative version of the icon.

    This is very similar to simple_print(), but reverses the printed characters.
    It loops over the icon_grid, unpacking the full list of lists. It
then unpacks
    each individual list, checks if each list item is a 1 or 0, then prints the
    "negative" character for each value. It uses space separators and return
    characters to space the output text in a pleasing manner.
    '''
    icon_grid = icon
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

def main():
# Open the hard coded binary file and assign it to a variable
    from_a_file = open_external_file()
# Take the binary variable and compact it into a 10x10 grid
    new_grid_icon = configure_file(from_a_file)
# Ask the user what their 'on' value is in the text file
    full_value = user_binary_symbol_on()
# Print the menu, asking the user which version of the image they want
    user_choice = icon_menu()
# Based on user input. print the version of the icon
    if user_choice == "1":
        simple_print(new_grid_icon, full_value)
    if user_choice == "2":
        mirror_print(new_grid_icon, full_value)
    if user_choice == "3":
        negative_print(new_grid_icon, full_value)

if __name__ == "__main__":
    main()
