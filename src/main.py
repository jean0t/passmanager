from termcolor import colored
from getpass import getpass
from database.database import database
from message import Message
from random_password import Password
from config import Config
from os import system
import sys
from time import sleep

class Passmanager():
    def __init__(self):
        Config.configure_environment(Config.app_path)
        self.database = None

    def Login(self):
        system("clear")
        password = getpass(colored("Enter your password: ", "light_red"))
        try:
            self.database = Password(password=password)
            Message.Success("User authenticated!")
            sleep(2)
        except:
            Message.Failure("User couldn't be authenticated!")
            sleep(2)
            sys.exit(1)


    def Menu(self):
        pass


    def Exit(self):
        self.database.Close()
