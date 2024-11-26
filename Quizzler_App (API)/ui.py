from tkinter import *

THEME_COLOR = "#375362"

class PlayerInterface:
    def __init__(self):
        self.window=Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas=Canvas(width=300,height=250,bg='white')
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)

        #score
        self.label=Label(text="Score: 0")
        self.label.config(bg=THEME_COLOR,fg='white',font=('Arial',15,'normal'))
        self.label.grid(row=0,column=1,sticky=E,pady=20)

        #Question
        self.text=self.canvas.create_text(150,125,text="Amazon acquired Twitch in August 2014 for $970 million dollars"
                                          ,font=('Arial',20,'italic'),width=280)

        #buttons
        self.green_pic = PhotoImage(file='./images/true.png')
        self.red_pic=PhotoImage(file='./images/false.png')

        self.true_button=Button(image=self.green_pic,highlightthickness=0,borderwidth=0)
        self.true_button.grid(row=2,column=0)





        self.window.mainloop()

