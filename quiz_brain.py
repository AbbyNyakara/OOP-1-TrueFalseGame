class QuizBrain:
    # Everytime the quizbrain object is called, it will require an input in the initialized method. This is the meaning
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    # the next_question method. the self highlighted in the parenthesis
    # simply shows that it belongs to a class(quizbrain). In this case, this is called a method.

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.question_text}. (True/False)?: ")
        correct_answer = current_question.question_answer
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer is  {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")
