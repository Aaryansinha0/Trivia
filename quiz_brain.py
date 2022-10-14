
class QuizBrain:

    def __init__(self, q_list):
        self.question_no = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            print("Quiz over!")
            print(f"Your final score is: {self.score}/{self.question_no}")
            return False

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        player_answer = input(f"Q.{self.question_no}: {current_question.text} (True/False) ")
        self.check_answer(player_answer, current_question.answer)

    def check_answer(self, player_answer, correct_answer):
        if player_answer.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1
        else:
            print("You are wrong!")
        print(f"The correct answer is {correct_answer}")
        print(f"Your score is: {self.score}/{self.question_no}")
        print("\n")
