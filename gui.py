from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("vatsal")
window.configure(background='cyan')
window.geometry('400x400')
window.resizable(False,False)
img=PhotoImage(file="")
def msg():
    messagebox.showwarning(message='hello')
Label(window,text="vatsal",
      fg='red',
      bg='blue',
      font='bold',
      ).pack()
e = Entry(window,
          fg='red',
          font='bold',
          show='*').pack(fill=X)
Checkbutton(window,text="male", bg='red', justify='center').pack(fill=X)
Button(command=msg,
       fg='red',
       bg='yellow',
       text="button",
       justify='center',
       ).pack(fill=X)
window.mainloop()