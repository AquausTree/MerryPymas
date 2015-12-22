import time, random
from random import randint


def mainmenu():
    start = input("Would you like to: 'Open Presents' or 'Open Inventory'")
    if start.lower() == "open presents": #Present Opening
        select = input("What type do you wish to open: \n- Jingle Gift")
        if select.lower() == "jingle gift":
            #todo: create random gift opening (randint)
            mainmenu()
    if start.lower() == "open inventory": #Open Inventory
        #todo: create working inventory (sql?)
        mainmenu()

print("Welcome to Merry Pymas! A game where you open presents and complete present collections!\n")
mainmenu()
