from tkinter import *
import ast

root = Tk()
i = 0
def get_num(num):
    global i
    display.insert(i, num)
    i += 1

def get_opration(oprator):
    global i
    length = len(oprator)
    display.insert(i, oprator)
    i += length

def clear_all():
    display.delete(0, END)

def calculate():
    entire_string = display.get()
    try:
        node = ast.parse(entire_string, mode= "eval")
        result = eval(compile(node, '<string>', 'eval'))
        clear_all()
        display.insert(0, result)
    except:
        clear_all()
        display.insert(0, "Error")

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0, "")

display = Entry(root, borderwidth=4)
display.grid(row=1, columnspan=6, pady = 20)


numbers = [1,2,3,4,5,6,7,8,9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root, text= button_text, width=4, height=2, pady=5, padx=5, borderwidth=4, command=lambda text = button_text: get_num(text))
        button.grid(row = x+4, column= y)
        counter += 1

button = Button(root, text="0", width=4, height=2, pady=5, padx=5, borderwidth=4 , command=lambda : get_num(0))
button.grid(row=7, column = 1)

count = 0
oprations = ['+', "-", "*", "/", "*3.14", "%", "(", "**", ")", "**2", "**3"]
for x in range(4):
    for y in range(3):
        if count < len(oprations):
            button = Button(root, text= oprations[count], width=4, height=2, pady=5, padx=5, borderwidth=4, command= lambda text  = oprations[count]: get_opration((text)))
            count += 1
            button.grid(row=x + 4, column=y+3)

button = Button(root,text="AC", width=4, height=2, pady=5, padx=5, borderwidth=4, command= clear_all ).grid(row = 7, column = 0)
button = Button(root,text="=", width=4, height=2, pady=5, padx=5, borderwidth=4, command= calculate).grid(row = 7, column = 2)
button = Button(root,text="<-",width=4, height=2, pady=5, padx=5, borderwidth=4, command= lambda : undo()).grid(row = 7, column = 5)

root.geometry("300x300")

root.mainloop()