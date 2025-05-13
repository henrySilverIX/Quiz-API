from tkinter import *
import sys
import os


THEME_COLOR = "#375362"




class QuizInterface:
    def __init__(self):
        #Window configuration
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(background=THEME_COLOR, pady=20, padx=20)

        #Label
        self.score = Label(text="Score: 0", background=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1, pady=20)


        #Canvas
        self.canvas = Canvas(width=300, height=250)
        self.canvas.create_text(150, 175, text="Zebras are white with black stripes", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, columnspan=2)



        #Buttons
        true_icon = PhotoImage(file=self.resource_path("images/true.png"))
        self.true_button = Button(image=true_icon, highlightthickness=0, bg=THEME_COLOR)
        self.true_button.grid(row=2, column=1, pady=20)

        false_icon = PhotoImage(file=self.resource_path("images/false.png"))
        self.true_button = Button(image=false_icon, highlightthickness=0, bg=THEME_COLOR)
        self.true_button.grid(row=2, column=0, pady=20)



        #Main loop to keep the window working
        self.window.mainloop()



    # Função to find the path correctly
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        if getattr(sys, 'frozen', False):
            # Executável
            return os.path.join(sys._MEIPASS, relative_path)
        else:
            # Script normal
            return os.path.join(os.path.abspath("."), relative_path)