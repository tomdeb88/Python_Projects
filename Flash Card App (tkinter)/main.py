from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
import sys


from pandas.core.interchange.dataframe_protocol import DataFrame

BACKGROUND_COLOR = "#B1DDC6"

try:
    df=pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    df = pd.read_csv('./data/french_words.csv')
finally:
    words_list=df.to_dict(orient='records')

random_pair={}

def green_button_pressed():
    words_list.remove(random_pair)
    if len(words_list)<1:
        messagebox.showinfo(title='You got it',message="There is no more words left to learn")
        sys.exit()
    data=pd.DataFrame(words_list)
    data.to_csv("./data/words_to_learn.csv",index=False)
    display_new_word()



def display_new_word():
    global random_pair, timer,words_list
    window.after_cancel(timer)
    random_pair = random.choice(words_list)
    canvas.itemconfig(bottom_text, text=random_pair['French'],fill='black')
    canvas.itemconfig(top_text, text='French',fill='black')
    canvas.itemconfig(background,image=front_card)
    timer=window.after(3000,eng_card)






def eng_card():
    canvas.itemconfig(background,image=back_card)
    canvas.itemconfig(bottom_text,fill='white', text=random_pair['English'])
    canvas.itemconfig(top_text,fill='white', text='English')


window=Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
timer=window.after(3000,eng_card)

#Canvas
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_card=PhotoImage(file='./images/card_front.png')
back_card=PhotoImage(file='./images/card_back.png')
background=canvas.create_image(400,263,image=front_card)
canvas.grid(column=0,row=0,columnspan=2)

#Texts
top_text=canvas.create_text(400,150,text="Title",font=('Ariel',40,'italic'))
bottom_text=canvas.create_text(400,263,text="word",font=('Ariel',60,'bold'))

#Buttons
x_button_image=PhotoImage(file='./images/wrong.png')
x_button=Button(image=x_button_image,highlightthickness=0,borderwidth=0,command=display_new_word)
x_button.grid(column=0,row=1)

y_button_image=PhotoImage(file='./images/right.png')
y_button=Button(image=y_button_image,highlightthickness=0,borderwidth=0,command=green_button_pressed)
y_button.grid(column=1,row=1)



display_new_word()
window.mainloop()

