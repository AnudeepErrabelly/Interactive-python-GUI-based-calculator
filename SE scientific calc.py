#!/usr/bin/env python
# coding: utf-8

# In[24]:


from tkinter import *
import math

def on_click(inputvalue):
    ex = entryField.get()  # 789 ex[0:len(ex)-1]
    answer = ''

    try:

        if inputvalue== 'C':
            ex = ex[0:len(ex) - 1]  # 78
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif inputvalue == 'CE':
            entryField.delete(0, END)

        elif inputvalue == '√':
            answer = math.sqrt(eval(ex))

        elif inputvalue == 'π':
            answer = math.pi

        elif inputvalue == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))

        elif inputvalue == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))

        elif inputvalue == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))

        elif inputvalue == '2π':
            answer = 2 * math.pi

        elif inputvalue == 'cosh':
            answer = math.cosh(eval(ex))

        elif inputvalue == 'tanh':
            answer = math.tanh(eval(ex))

        elif inputvalue == 'sinh':
            answer = math.sinh(eval(ex))

        elif inputvalue == chr(8731):
            answer = eval(ex) ** (1 / 3)

        elif inputvalue == 'x\u02b8':  # 7**2
            entryField.insert(END, '**')
            return

        elif inputvalue == 'x\u00B3':
            answer = eval(ex) ** 3

        elif inputvalue == 'x\u00B2':
            answer = eval(ex) ** 2

        elif inputvalue == 'ln':
            answer = math.log2(eval(ex))
        elif inputvalue == 'deg':
            answer = math.degrees(eval(ex))

        elif inputvalue == "rad":
            answer = math.radians(eval(ex))

        elif inputvalue == 'e':
            answer = math.e

        elif inputvalue == 'log₁₀':
            answer = math.log10(eval(ex))

        elif inputvalue == 'x!':
            answer = math.factorial(ex)

        elif inputvalue == chr(247):  # 7/2=3.5
            entryField.insert(END, "/")
            return

        elif inputvalue == '=':
            answer = eval(ex)

        else:
            entryField.insert(END, inputvalue)
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)

    except SyntaxError:
        pass

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def mul(a, b):
    return a * b
def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def lcm(a,b):
    l=math.lcm(a,b)
    return l

def hcf(a,b):
    h=math.gcd(a,b)
    return h

operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
            'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
            'PRODUCT': mul, 'MULTIPLICATION': mul,'MULTIPLY': mul,
            'DIVISION': div, 'DIV': div, 'DIVIDE': div,
            'LCM':lcm , 'HCF':hcf,
            'MOD':mod ,'REMAINDER':mod , 'MODULUS':mod }


def findNumbers(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l



gui_root = Tk()
gui_root.title('Smart Calculator')
gui_root.config(bg='dodgerblue3')
gui_root.geometry('800x800+30+30')

logoLabel = Label(gui_root, bg='dodgerblue3')
logoLabel.grid(row=0, column=0)

entryField = Entry(gui_root, font=('arial', 20, 'bold'), bg='dodgerblue3', fg='white', bd=10, relief=SUNKEN, width=30)
entryField.grid(row=0, column=0, columnspan=8)



button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
rowvalue = 1
columnvalue = 0
for i in button_text_list:

    button = Button(gui_root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='dodgerblue3', fg='black',
                    font=('arial', 16, 'bold'), activebackground='dodgerblue3', command=lambda button=i: on_click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

gui_root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




