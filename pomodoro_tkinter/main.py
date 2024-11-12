import math
from tkinter import *


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK_STRING="✔"
reps=0
timer_clock=None
ticked=''




def reset_app():
    global reps
    timer_label.config(text='Timer',fg=GREEN)
    canvas.itemconfig(timer, text="00:00")
    window.after_cancel(timer_clock)
    checkmark.config(text='')
    reps=0


def start_timer():
    global reps
    reps+=1

    if reps % 8==0:
        counting_down(LONG_BREAK_MIN*60)
        timer_label.config(text='Break',fg=RED)
    elif reps % 2 ==0:
        counting_down(SHORT_BREAK_MIN*60)
        timer_label.config(text='Break',fg=PINK)
    else:
        counting_down(WORK_MIN*60)
        timer_label.config(text='Work',fg=GREEN)




def counting_down(number):
    global ticked
    minutes=math.floor(number/60)
    seconds=number % 60

    if seconds<10:
        seconds=f'0{seconds}'
    canvas.itemconfig(timer,text=f"{minutes}:{seconds}")
    if number>0:
        global timer_clock
        timer_clock= window.after(1000,counting_down,number-1)
    else:
        start_timer()
        if reps % 2==0:
            ticked+=CHECKMARK_STRING
            checkmark.config(text=ticked)




window=Tk()
window.title('Pomodoro App')
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_pic=PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_pic)
timer=canvas.create_text(100,128,text="00:00",fill='white',font=(FONT_NAME,30,'bold'))
canvas.grid(column=1,row=1)

#Timer label
timer_label=Label(text='Timer',bg=YELLOW,font=(FONT_NAME,30,'bold'),fg=GREEN)
timer_label.grid(column=1,row=0)

#Buttons
start_button=Button(text="Start",command=start_timer)
start_button.config(pady=1,padx=5)
start_button.grid(column=0,row=2)

reset_button=Button(text='Reset',command=reset_app)
reset_button.config(pady=1,padx=5)
reset_button.grid(column=2,row=2)

#Checkmarks
checkmark=Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,20,'bold'))
checkmark.grid(column=1,row=3)



window.mainloop()
