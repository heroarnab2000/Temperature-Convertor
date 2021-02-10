#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Created by: Arnab Das
Date: 10-02-2021
Time: 04:48 PM

Feel free to use for academic purposes only.

"""


from tkinter import *

conv = Tk()
conv.geometry('500x250')
conv.title("Temperature Convertor")

textinC = StringVar()
textinF = StringVar()

def convert():
    
    global textinC
    global textinF
    
    sC = textinC.get()
    sF = textinF.get()
    
    if sC:
        sf = round((float(sC) * 9/5) + 32, 5)
        textinF.set(sf)
    elif sF:
        sc = round((float(sF) - 32) * 5/9, 5)
        textinC.set(sc)

        
def clear():
    
    global textinC
    global textinF
    
    sC = ""
    sF = ""
    textinC.set('')
    textinF.set('')
        
labelname = Label(conv, text = "Temperature Convertor", width = 20, font = ("bold", 20))
labelname.place(x = 90,y = 00)

Label(conv, text = 'In Centrigrade:', font = ("Courier New",12,'bold')).place(x = 90,y = 60)
Label(conv, text = 'In Fahrenheit:', font = ("Courier New",12,'bold')).place(x = 270,y = 60)

e_1 = Entry(conv, textvariable = textinC, width = 20,bd = 2, bg = 'powder blue').place(x = 100,y = 90)
e_2 = Entry(conv, textvariable = textinF, width = 20,bd = 2, bg = 'powder blue').place(x = 280,y = 90)

Cl = Button(conv, text = "Clear", command = clear, font = 'Times')
Cl.place(x = 175, y = 150)

Conv = Button(conv, text = "Convert", command = convert, font = 'Times')
Conv.place(x = 270, y = 150)

exit = Button(conv, text = "EXIT", command = conv.destroy, font = 'Times')
exit.place(x = 225, y = 200)


conv.mainloop()

