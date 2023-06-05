from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q1 = question['text']
    answer = question['answer']
    new_question = Question(q1, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print('You completed the quiz Well Done!')
print(f'Your final scores was:{quiz.score}/{quiz.question_number} ')
