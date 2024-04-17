from tkinter import*
import sys
class MyOptionMenu(OptionMenu):
    def __init__(self, master, status, *options):
        self.var = StringVar(master)
        self.var.set(status)
        OptionMenu.__init__(self, master, self.var, *options)
        global arrow
        arrow = PhotoImage(file=sys.path[1]+"/Tekinta/arrow.png")
        self['menu'].config(font=('calibri',(10)),bg='white')
        self.config(font=('calibri',(10)),bg='white',indicatoron=False,compound='right',image=arrow,width=200)

root = Tk()
#mymenu1 = MyOptionMenu(root, 'Select status', 'a','b','c')
mymenu2 = MyOptionMenu(root, 'Select another status    ', 'd','e','f')
#mymenu1.pack()
mymenu2.pack()
mymenu3 = MyOptionMenu(root, 'Select another status    ', 'd','e','f')

mymenu3.pack()
root.mainloop()
