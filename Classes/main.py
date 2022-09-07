from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_q = Question(question["text"], question["answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("you've finished the quiz ")
print(f"Your final score was {quiz.score}/{len(question_bank)}")
