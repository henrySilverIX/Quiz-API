from tkinter import *
import sys
import os
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain_v: QuizBrain):
        self.quiz_question = quiz_brain_v
        #Window configuration
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(background=THEME_COLOR, pady=20, padx=20)

        #Label
        self.score = Label(text="Score: 0", background=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1, pady=20)


        #Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Some question text", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)



        #Buttons
        true_icon = PhotoImage(file=self.resource_path("images/true.png"))
        self.true_button = Button(image=true_icon, highlightthickness=0, bg=THEME_COLOR, command=self.mark_true)
        self.true_button.grid(row=2, column=1, pady=20)

        false_icon = PhotoImage(file=self.resource_path("images/false.png"))
        self.false_button = Button(image=false_icon, highlightthickness=0, bg=THEME_COLOR, command=self.mark_false)
        self.false_button.grid(row=2, column=0, pady=20)

        # Update the question text on canvas
        self.get_next_question()

        #Main loop to keep the window working
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz_question.still_has_questions():
            self.canvas.config(background="white")
            self.score.config(text=f"Score: {self.quiz_question.score}")
            q_text = self.quiz_question.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(background="white")
            self.canvas.itemconfig(self.question_text, text=f"End of the game\nFinal Score: {self.quiz_question.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")



    def mark_true(self):
        self.feedback(self.quiz_question.check_answer("True"))

    def mark_false(self):
        self.feedback(self.quiz_question.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)



    # Função to find the path correctly
    def resource_path(self, relative_path):
        """ Get an absolute path to resource, works for dev and for PyInstaller """
        if getattr(sys, 'frozen', False):
            # Executável
            return os.path.join(sys._MEIPASS, relative_path)
        else:
            # Script normal
            return os.path.join(os.path.abspath("."), relative_path)

