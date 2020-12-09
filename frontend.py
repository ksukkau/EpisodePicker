from tkinter import *
import backend

def Random_command():
    list1.delete(0, END)
    for row in backend.episode():
        list1.insert(END, row)

def TOS_command():
    list1.delete(0, END)
    for row in backend.TOS():
        list1.insert(END, row)

def TNG_command():
    list1.delete(0, END)
    for row in backend.TNG():
        list1.insert(END, row)

def VOY_command():
    list1.delete(0, END)
    for row in backend.VOY():
        list1.insert(END, row)

def DIS_command():
    list1.delete(0, END)
    for row in backend.DIS():
        list1.insert(END, row)

def TAS_command():
    list1.delete(0, END)
    for row in backend.TAS():
        list1.insert(END, row)

def DS9_command():
    list1.delete(0, END)
    for row in backend.DS9():
        list1.insert(END, row)

def ENT_command():
    list1.delete(0, END)
    for row in backend.ENT():
        list1.insert(END, row)

def PIC_command():
    list1.delete(0, END)
    for row in backend.PIC():
        list1.insert(END, row)

window = Tk()
window.wm_title("Star Trek Episode Picker")

l1=Label(window, text="Pick a series")
l1.grid(row=0, column=0,rowspan=1, columnspan=2)

b1=Button(window, text= "Random", width= 24, command=Random_command)
b1.grid(row=1, column=0,rowspan=1, columnspan=2)

b2=Button(window, text= "The Original Series", width= 24, command=TOS_command)
b2.grid(row=2, column=0)

b3=Button(window, text= "The Animated Series", width= 24, command=TAS_command)
b3.grid(row=2, column=1)

b4=Button(window, text= "The Next Generation", width= 24, command=TNG_command)
b4.grid(row=3, column=0)

b5=Button(window, text= "Deep Space Nine", width= 24, command=DS9_command)
b5.grid(row=3, column=1)

b6=Button(window, text= "Voyager", width= 24, command=VOY_command)
b6.grid(row=4, column=0)

b7=Button(window, text= "Enterprise", width= 24, command=ENT_command)
b7.grid(row=4, column=1)

b8=Button(window, text= "Discovery", width= 24, command=DIS_command)
b8.grid(row=5, column=0)

b9=Button(window, text= "Picard", width= 24, command=PIC_command)
b9.grid(row=5, column=1)


list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=4, rowspan=4, columnspan=1)

l2=Label(window, text="Series\nEpisode\nName\nStardate")
l2.grid(row=2, column=3,rowspan=3)


window.mainloop()