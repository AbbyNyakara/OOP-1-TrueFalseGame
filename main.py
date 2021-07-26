from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# question_bank = []
# for question in question_data:
#     question_bank.append(question)
# print(question_bank)

question_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    # New question object
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

# Create a quiz object
quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the challenge.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
