from database import Database
from random import randint
from uuid import uuid4


class Question(object):

    def __init__(self, question, a_1, a_2, a_3, a_4, true_anserw, value, _id=uuid4().hex):
        self._id = _id
        self.question = question
        self.a_1 = a_1
        self.a_2 = a_2
        self.a_3 = a_3
        self.a_4 = a_4
        self.true_anserw = true_anserw
        self.value = value

    def json(self):
        return {
            '_id': self._id,
            'question': self.question,
            'a_1': self.a_1,
            'a_2': self.a_2,
            'a_3': self.a_3,
            'a_4': self.a_4,
            'true_anserw': self.true_anserw,
            'value': self.value
        }

    def add_question(self):
        Database.insert(collection='quiz', data=self.json())

    @classmethod
    def get_question(cls, value):
        questions = [q for q in Database.find(collection='quiz', query={'value': value})]
        random = randint(0, len(questions) - 1)
        question_data = questions[random]

        return cls(**question_data)

    @classmethod
    def adding_scheme(cls):
        question = input("Enter the question: ")
        a_1 = input("Enter the first anserw: ")
        a_2 = input("Enter the second anserw: ")
        a_3 = input("Enter the third anserw: ")
        a_4 = input("Enter the fourth anserw: ")
        true_anserw = input("Enter the true anserw: ")
        value = input("Enter the value of question: ")
        return cls(question=question, a_1=a_1, a_2=a_2, a_3=a_3, a_4=a_4, true_anserw=true_anserw, value=value)

    @staticmethod
    def adding_procedure():
        adding_success = False
        while not adding_success:
            admin_quest = input('Do you want to add (A) a question or start (enter) a game?')
            if admin_quest == "A":
                question = Question.adding_scheme()
                question.add_question()
            else:
                adding_success = True
