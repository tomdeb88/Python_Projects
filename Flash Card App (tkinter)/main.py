from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

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
bottom_text=canvas.create_text(400,263,text="Word",font=('Ariel',60,'bold'))



#Buttons
x_button_image=PhotoImage(file='./images/wrong.png')
x_button=Button(image=x_button_image,highlightthickness=0,borderwidth=0)
x_button.grid(column=0,row=1)

y_button_image=PhotoImage(file='./images/right.png')
y_button=Button(image=y_button_image,highlightthickness=0,borderwidth=0)
y_button.grid(column=1,row=1)

















window.mainloop()

