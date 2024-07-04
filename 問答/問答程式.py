import json
import random


class Question:
    def __init__(self, description, answer):
        self.description = description
        self.answer = answer

    def ask(self):
        print(self.description)
        user_answer = input("答:")
        if user_answer == self.answer:
            return True
        else:
            return False


class QuestionGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def play(self):
        j = 0
        for question in self.questions:
            j += 1
            if question.ask():
                print("恭喜答對")
                self.score += 1
            else:
                print(f"答錯了 正確答案為{question.answer}")
        print(f"\n總共{j}題 答對了{self.score}題")

    def random_pick(self, num):
        ran_q = []
        for i in range(0, num):
            selection = self.questions[random.randint(0, len(self.questions)-1)]
            ran_q.append(selection)

        return ran_q


with open("question.json", "r", encoding="utf-8") as file:
    ques = json.loads(file.read())


for i in range(0, len(ques)):
    ques[i] = Question(ques[i]["description"], ques[i]["answer"])

question_base = QuestionGame(ques)
get_ran = question_base.random_pick(int(input("測驗題數")))
random_question = QuestionGame(get_ran)
random_question.play()