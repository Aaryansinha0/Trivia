from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    q_text = data["question"]
    q_answer = data["correct_answer"]
    questions = Question(data["question"], data["correct_answer"])
    question_bank.append(questions)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
