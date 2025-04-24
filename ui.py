from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:



    def __init__(self, quiz_brain: QuizBrain):  # you define this parameter's data type is object from Class QuizBrain only
        self.quiz = quiz_brain  # this is an object from class QuizBrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # Score label
        self.score = 0
        self.score_label = Label(
            text=f"Score: {self.score}",
            fg="white",  # text color
            background=THEME_COLOR,  # background == bg
            font=("Arial", 20, "italic"))
        self.score_label.grid(row=0, column=1)

        # Your Board that your write inside it a questions
        self.my_Board = Canvas(width=300, height=250, bg="white")
        self.question_text = self.my_Board.create_text(
            150,  # x position
            125,  # y position
            width=280,
            text="Some Questions text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))  # Don't Forget the position of text
        self.my_Board.grid(row=1, column=0, columnspan=2, pady=50)  # Don't forget to make padding

        # Buttons
        t_Photo = PhotoImage(file="images/true.png")
        self.true_button = Button(image=t_Photo, highlightthickness=0, command=self.is_true)
        self.true_button.grid(row=2, column=0)

        f_Photo = PhotoImage(file="images/false.png")
        self.false_button = Button(image=f_Photo, highlightthickness=0, command=self.is_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.my_Board.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.my_Board.itemconfig(self.question_text, text=q_text)
        else:
            self.my_Board.itemconfig(self.question_text, text="You've reached the end of quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def is_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def is_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        # we can't use time.sleep() because window.mainloop()
        if is_right:
            self.my_Board.config(bg="green")
        else:
            self.my_Board.config(bg="red")

        self.window.after(1000, self.get_next_question)

