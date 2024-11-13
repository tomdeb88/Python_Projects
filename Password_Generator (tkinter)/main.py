from tkinter import *

# ---------------------saving passwords----------------


















#-----------------UI----------------------
window=Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)
canvas=Canvas(width=200,height=220,highlightthickness=0)
logo=PhotoImage(file='new_lock.png')
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

#Label
web_label=Label(text="Website:")
web_label.grid(column=0,row=1)
email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label=Label(text="Password:")
password_label.grid(column=0,row=3)


#Entries
web_entry=Entry(width=35)
web_entry.focus()
web_entry.grid(column=1,row=1,columnspan=2,pady=5)
email_entry=Entry(width=35)
email_entry.insert(0,'tomdeb00@protonmail.com')
email_entry.grid(column=1,row=2,columnspan=2,pady=5)

password_entry=Entry(width=21)
password_entry.grid(column=1,row=3,pady=5,sticky=W)


#Buttons
gen_button=Button(text='Generate')
gen_button.grid(column=2,row=3)


add_button=Button(text="Add",width=33)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()