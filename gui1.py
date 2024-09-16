from tkinter import *
window = Tk()
window.resizable(False,False)
window.configure(background='red')

Button(window,text="1",width='10').grid(row='0',column='0')
Button(window,text="2",width='10').grid(row='0',column='1')
Button(window,text="3",width='10').grid(row='0',column='2')
Button(window,text="4",width='10').grid(row='1',column='0')
Button(window,text="5",width='10').grid(row='1',column='1')
Button(window,text="6",width='10').grid(row='1',column='2')
Button(window,text="7",width='10').grid(row='2',column='0')
Button(window,text="8",width='10').grid(row='2',column='1')
Button(window,text="9",width='10').grid(row='2',column='2')
e=Entry(window,bg='red',width='30').grid(row='3',columnspan='3')

window.mainloop()