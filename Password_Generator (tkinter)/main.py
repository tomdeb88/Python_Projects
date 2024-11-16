from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def search():
    text=web_entry.get()
    try:
        with open('/home/tomasz/Desktop/passd/passwd.json', 'r') as file:
            websites=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message='No Data File Found')
    else:
        if text  in websites.keys():
            messagebox.showinfo(title=text, message=f'Email: {websites[text]['email']}\nPassword: {websites[text]['password']}')
            pyperclip.copy(websites[text]['password'])

        else:
            messagebox.showinfo(title="Error", message='No details for the website exists')


#---------------generating password--------------------
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    num_letters=random.randint(8,10)
    num_numbers=random.randint(2,4)
    num_symbols=random.randint(2,4)
    password_list=[random.choice(letters) for char in range(num_letters)]
    password_list+=[random.choice(numbers) for char in range(num_numbers)]
    password_list+=[random.choice(symbols) for char in range(num_symbols)]
    random.shuffle(password_list)

    password_entry.delete(0,END)
    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)



# ---------------------saving passwords----------------
def add_passwd():
    web_name=web_entry.get()
    email_name=email_entry.get()
    password=password_entry.get()
    new_data={
        web_name:{
            'email':email_name,
            'password':password,
        }
    }

    if len(web_name)==0 and len(password)==0:
        messagebox.showinfo('Warning',"Your website and password fields can't be blank")
    elif len(web_name)==0:
        messagebox.showinfo("Warning","Your website field can't be blank")
    elif len(password)==0:
        messagebox.showinfo("Warning","Your password field can't be blank")
    else:
        try:
            with open('/home/tomasz/Desktop/passd/passwd.json', 'r') as file:
                data=json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open('/home/tomasz/Desktop/passd/passwd.json', 'w') as file:
                json.dump(new_data,file)

        else:
            with open('/home/tomasz/Desktop/passd/passwd.json', 'w') as file:
                json.dump(data,file,indent=4)

    web_entry.delete(0, END)
    password_entry.delete(0, END)


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
web_entry=Entry(width=21)
web_entry.focus()
web_entry.grid(column=1,row=1,pady=5,padx=4,sticky=W)
email_entry=Entry(width=35)
email_entry.insert(0,'tomdeb00@protonmail.com')
email_entry.grid(column=1,row=2,columnspan=2,pady=5)

password_entry=Entry(width=21)
password_entry.grid(column=1,row=3,pady=5,padx=3,sticky=W)


#Buttons
gen_button=Button(text='Generate',command=generate_password)
gen_button.grid(column=2,row=3)


add_button=Button(text="Add",width=33,command=add_passwd)
add_button.grid(row=4,column=1,columnspan=2)

search_button=Button(text="Search",padx=20,bg='#8068EF',command=search)
search_button.grid(column=2,row=1)



window.mainloop()

