from modules.login import Login
from modules.test import Test
from modules.question import Question


class Menu(object):
    def __init__(self):
        print('Welcome to the Milionaries')
        quest = input("Do you want to login in (L) or sign up (S)?: ")
        successful_login = False
        if quest == "L":
            while not successful_login:
                self.username = input("Enter your username: ")
                self.password = input("Enter your password: ")
                if Login.check_login(self.username, self.password):
                    if Login.check_admin(self.username):
                        Question.adding_procedure()
                    successful_login = True
                else:
                    print("Invalid username or password.")
            else:
                print("Welcome to the platform")
                test = Test(self.username)
                test.run_test()

        elif quest == "S":
            if_account_create = False
            while not if_account_create:
                self.username = input("Enter your username: ")
                self.password = input("Enter your password: ")
                self.admin = Login.register_admin()

                if Login.find_user(self.username) is None:
                    Login.create_account(self.username, self.password, self.admin)
                    test = Test(self.username)
                    test.run_test()
                    if_account_create = True
                else:
                    register_quest = input(
                        'This username is already registered. If you want to try again just click enter or close '
                        'the app with "E": ')
                    if register_quest == "E" or register_quest == "e":
                        print('Thank you for using our app')
                        break


        else:
            print("You type the order wrong. Restart app and try again")
