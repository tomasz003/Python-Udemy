from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank=[]
for que in question_data:
    new_question=Question(que["text"], que["answer"])
    question_bank.append(new_question)

quiz=Quizbrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score: {quiz.score}/{quiz.question_number}.")