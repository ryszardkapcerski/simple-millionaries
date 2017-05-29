from modules.question import Question
import random


class Test(object):
    def __init__(self, username):
        self.username = username

    @staticmethod
    def run_test():

        levels = ["500", "1000", "2000", "5000", "10000", "20000", "40000", "75000", "125000", "250000", "1000000"]

        for l in levels:

            print('Now you can win {}'.format(l))
            choice = input("Do you want to answer (A) the question or end (E) the program?: ")

            if choice == "A":

                question = Question.get_question(l)
                answers = [question.a_1, question.a_2, question.a_3, question.a_4]
                answers_random = random.sample(answers, len(answers))  # mix answers
                answers_labels = ["A", "B", "C", "D"]
                print(question.question)
                for x in range(0, 4):
                    print("{}. {}".format(answers_labels[x], answers_random[x]))
                user_label = input("Select an anserw from A to D: ")
                if user_label in answers_labels:
                    user_anserw = answers_random[answers_labels.index(user_label)]
                    if user_anserw == question.true_anserw:
                        print("Your anserw is correct")
                    else:
                        print("Your anserw is incorrect. Restart your program to try again")
                        break
                else:
                    print("You typed incorrect label. Are sure it was A, B, C or D? Restart your program to try again")
                    break




            elif choice == "E":
                print("Thank you for using our platform")
                break
            else:
                print("The input is invalid. Try again.")
                break
        else:
            print('Congratulations you win the game')
