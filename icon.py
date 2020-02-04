# -*- coding: utf-8 -*-

def create_icon_grid():
    '''This static function defines variables with entries of 1 and 0 for each of the
    ten lines in the icon grid. 1s represent shaded cells and 0s represent empty
    cells. The individual lines are then packed into an icon_grid list. This list
    is returned by the function for use elsewhere. This function could be altered
    with hardcoded grid values for other printable icons.'''
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

def simple_print():
    '''This function does the simplest printing of the icon. It loops over the
    icon_grid, unpacking the full list of lists. It then unpacks each individual
    list, checks if each list item is a 1 or 0, then prints the appropriate 
    character for each value. It uses space separators and return characters 
    to space the output text in a pleasing manner.'''
    icon_grid = create_icon_grid()
    for line in icon_grid:
        for cell in line:
            if cell == 1:
                print("@", end=" ")
            else:
                print(" ", end=" ")
        print("\r")

def mirror_print():
    '''This function is very similar to the simple_print() function. It loops 
    over the icon_grid, unpacking the full list of lists. It then uses reverse()
    to reverse each list in place. After reversing a list, it loops over it,
    checking if each list item is a 1 or 0, then prints the appropriate character
    for each value. It uses space separators and return characters to space the 
    output text in a pleasing manner.'''
    icon_grid = create_icon_grid()
    for line in icon_grid:
        line.reverse()
        for cell in line:
            if cell == 1:
                print("@", end=" ")
            else:
                print(" ", end=" ")
        print("\r")

def negative_print():
    '''This is very similar to simple_print(), but reverses the printed characters.
    It loops over the icon_grid, unpacking the full list of lists. It then unpacks 
    each individual list, checks if each list item is a 1 or 0, then prints the
    "negative" character for each value. It uses space separators and return 
    characters to space the output text in a pleasing manner.'''
    icon_grid = create_icon_grid()
    for line in icon_grid:
        for cell in line:
            if cell == 1:
                print(" ", end=" ")
            else:
                print("@", end=" ")
        print("\r")

def icon_menu():
    '''This function displays a menu to the user that lets them choose how they'd
    like to see the icon printed. It validates their input and then returns it as
    a variable for use elsewhere.'''
    user_choice = ""
    while user_choice == "":
        user_choice = input(
        "Please select which version of the lovely swimming goose icon " + 
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

def icon_printer(user_choice):
    '''This function takes the user_choice variable from the icon_menu() function
    and calls the relevant print function for the choice they made.'''
    if user_choice == "1":
        simple_print()
    if user_choice == "2":
        mirror_print()
    if user_choice == "3":
        negative_print()

def main():
    user_choice = icon_menu()
    icon_printer(user_choice)

if __name__ == "__main__":
    main()