import tkinter

window=tkinter.Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=15,pady=15)

def calculate():
    miles=float(form.get())
    km=miles*1.6
    result['text']=round(km,2)


form=tkinter.Entry(width=10)
form.grid(column=1,row=0)


miles_label=tkinter.Label(text="Miles")
miles_label.config(padx=10)
miles_label.grid(column=2,row=0)

is_equal_to=tkinter.Label(text='is equal to')
is_equal_to.config(padx=10,pady=5)
is_equal_to.grid(column=0,row=1)


result=tkinter.Label(text=0)
result.grid(column=1,row=1)

km=tkinter.Label(text='Km')
km.config(padx=20,pady=5)
km.grid(column=2,row=1)


button=tkinter.Button(text="Calculate",command=calculate)
button.grid(column=1,row=2)





window.mainloop()