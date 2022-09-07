class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        current_q = self.questions_list[self.question_number]
        self.question_number += 1
        choice = input(
            f"Q.{self.question_number}  {current_q.text} (True/False): ")
        self.check_answer(choice, current_q.answer)

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, choice, correct_anwser):
        if choice.lower() == correct_anwser.lower():
            self.score += 1
            print("You are Right")
        else:
            print("You are Wrong")
            print(f"The correct answer was {correct_anwser}. ")
        print(f"Your score {self.score}/{self.question_number}")
        print("\n")
