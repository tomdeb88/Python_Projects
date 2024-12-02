from tkinter import *
from data import parameters
from quiz_brain import QuizBrain # for typing hints
from functools import partial
from tkinter import messagebox
import os

THEME_COLOR = "#375362"
change_bg=None

class PlayerInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas=Canvas(width=300,height=250,bg='white')
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        # Question
        self.text = self.canvas.create_text(150, 125,
                                            text=""
                                            ,font=('Arial', 20, 'italic'),fill=THEME_COLOR, width=280)

        #score
        self.label=Label(text="Score: 0")
        self.label.config(bg=THEME_COLOR,fg='white',font=('Arial',15,'normal'))
        self.label.grid(row=0,column=1,sticky=E,pady=20)

        #buttons
        self.green_pic = PhotoImage(file='./images/true.png')
        self.red_pic=PhotoImage(file='./images/false.png')

        self.true_button=Button(image=self.green_pic,highlightthickness=0,borderwidth=0,command=partial(self.check_user_answer,'True'))
        self.true_button.grid(row=2,column=0)

        self.false_button=Button(image=self.red_pic,highlightthickness=0,borderwidth=0,command=partial(self.check_user_answer,'False'))
        self.false_button.grid(row=2,column=1)



        self.get_next_question()
        self.window.mainloop()

    def bgc_color(self,color):
        self.canvas.configure(bg=color)


    def get_next_question(self):
        if self.quiz.still_has_questions():
            messagebox.showinfo("You've completed the quiz",
                                f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            os._exit(0)

        question_text=self.quiz.next_question()
        self.canvas.itemconfig(self.text,text=question_text)
        self.bgc_color('white')

    def check_user_answer(self,correct):
        if self.quiz.check_answer(correct):
            score=self.quiz.score
            self.label['text']=f"Score: {score}"
            self.bgc_color('green')
        else:
            self.bgc_color('red')
        self.window.after(1000, self.get_next_question)




