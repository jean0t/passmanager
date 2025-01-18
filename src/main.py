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
            sleep(1.5)
        except:
            Message.Failure("User couldn't be authenticated!")
            sleep(2)
            sys.exit(1)


    def Menu(self):
        Message.Info("Use the command 'help' to see the commands")
        while True:
            prompt = input("> ").strip().lowercase()

            match prompt:
                case "help":
                    Message.Info("generate -> generates a random password")
                    Message.Info("query_all -> see all password")
                    Message.Info("query_one [ID] -> see a specific password")
                    Message.Info("add -> add a new password to database")
                    Message.Info("update [ID] -> update the data")
                    Message.Info("remove [ID] -> remove a specific data (Be careful!)")
                    Message.Info("clear -> clear the screen")
                    Message.Info("exit -> leaves the program")
                
                case "generate":
                    pass

                case "query_one":
                    if len(prompt.split(" ")) == 2:
                        self.database.Query_one(int(prompt.split(" ")[1]))
                    else:
                        Message.Failure("Please provide an ID.")

                case "query_all":
                    self.database.Query_all()

                case "remove":
                    if len(prompt.split(" ")) == 2:
                        if input("Are you sure? (y/n) ").strip().lowercase() == "y":
                            self.database.Remove(int(prompt.split(" ")[1]))
                        else:
                            Message.Info("Operation aborted.")
                    else:
                        Message.Failure("Please provide an ID.")

                case "update":
                    if len(prompt.split(" ")) == 2:
                        self.database.Update(id= int(prompt.split(" ")[1]), username= input("username: ").strip(), password= input("password: ").strip(), comments= input("comments: ").strip())
                        Message.Success("Updated Successfuly.")
                    else:
                        Message.Failure("Please provide an ID.")

                case "add":
                    self.database.Add(username= input("username: ").strip(), password= input("password: ").strip(), comments= input("comments: ").strip())
                    Message.Success("Data added to database.")

                case "clear":
                    system("clear")


                case "exit":
                    self.database.Close()
                    exit(0)

    def Exit(self):
        self.database.Close()
