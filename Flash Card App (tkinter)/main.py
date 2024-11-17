from random import random
from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

df=pd.read_csv('./data/french_words.csv')
words_list=df.to_dict(orient='records')


def display_new_word():
    random_pair = random.choice(words_list)
    canvas.itemconfig(bottom_text, text=random_pair['French'])
    canvas.itemconfig(top_text, text='French')










window=Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

#Canvas
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_card=PhotoImage(file='./images/card_front.png')
canvas.create_image(400,263,image=front_card)
canvas.grid(column=0,row=0,columnspan=2)

#Texts
top_text=canvas.create_text(400,150,text="Title",font=('Ariel',40,'italic'))
bottom_text=canvas.create_text(400,263,text="word",font=('Ariel',60,'bold'))

#Buttons
x_button_image=PhotoImage(file='./images/wrong.png')
x_button=Button(image=x_button_image,highlightthickness=0,borderwidth=0,command=display_new_word)
x_button.grid(column=0,row=1)

y_button_image=PhotoImage(file='./images/right.png')
y_button=Button(image=y_button_image,highlightthickness=0,borderwidth=0,command=display_new_word)
y_button.grid(column=1,row=1)




display_new_word()
window.mainloop()

