# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 18:58:07 2020

@author: joel.whiteman
"""

import random

class Account:
    """Account class for maintaining a bank account"""

    def __init__(self, name, balance):
        """Initialize an Account object"""
        self.name = name
        self.balance = balance
        self.fav_color = "orange"
        self.__user_id = random.randint(pow(10, 5), pow(10, 8))

    def deposit(self, amount):
        """Deposit money to the account"""
        self.balance += amount
        
    def ask_for_fav_color(self):
        self.fav_color = input("What is your favorite color?\n")

# Create an instance of a class
james_account = Account('James Gosling', 20000000)

# Let's deposit some money in there
james_account.deposit(500)
james_account.ask_for_fav_color()

# Let's see Eric's balance
print(james_account.balance)
print(james_account.fav_color)

# Let's try seeing Eric's user_id (this will throw an error)
# print(james_account.__user_id)