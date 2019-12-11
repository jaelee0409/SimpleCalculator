#!/usr/bin/python3
from tkinter import *
from collections import deque

root = Tk()
root.title("My Calculator")
root.resizable(height = 0, width = 0)

en = Entry(root, width=35, borderwidth=5)
en.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

stack = deque()

def button_number(number):
    current = en.get()
    en.delete(0, END)
    en.insert(0, str(current) + str(number))

def button_add():
    stack.append(int(en.get()))
    stack.append('+')
    en.delete(0, END)

def button_subtract():
    stack.append(int(en.get()))
    stack.append('-')
    en.delete(0, END)

def button_multiply():
    stack.append(int(en.get()))
    stack.append('*')
    en.delete(0, END)

def button_divide():
    stack.append(int(en.get()))
    stack.append('/')
    en.delete(0, END)

def button_modulo():
    stack.append(int(en.get()))
    stack.append('%')
    en.delete(0, END)

def calculate():
    op_stack = deque()
    rpn_stack = deque()
    current_number = int(en.get())
    stack.append(current_number)
    en.delete(0, END)
    # to Reverse Polish notation
    for x in stack:
        if x == '+' or x == '-':
            if op_stack:
                rpn_stack.append(op_stack.pop())
            op_stack.append(x)
        elif x == '*' or x == '/' or x == '%':
            while op_stack and (op_stack[-1] == '*' or op_stack[-1] == '/' or op_stack[-1] == '%'):
                rpn_stack.append(op_stack.pop())
            op_stack.append(x)
        else:
            # x is a number
            rpn_stack.append(x)
    while op_stack:
        rpn_stack.append(op_stack.pop())

    # calculate result with RPN
    stack.clear()
    for x in rpn_stack:
        if x == '+':
            stack.append(stack.pop() + stack.pop())
        elif x == '-':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2 - num1)
        elif x == '*':
            stack.append(stack.pop() * stack.pop())
        elif x == '/':
            num1 = stack.pop()
            if num1 == 0:
                # no division by 0
                exit(0)
            num2 = stack.pop()
            stack.append(num2 / num1)
        elif x == '%':
            num1 = stack.pop()
            if num1 == 0:
                # no modulo by 0
                exit(0)
            num2 = stack.pop()
            stack.append(num2 % num1)
        else:
            # x is a number
            stack.append(x)
    en.insert(0, stack.pop())
    # clear all stacks
    stack.clear()
    op_stack.clear()
    rpn_stack.clear()

def button_clear():
    en.delete(0, END)
    stack.clear()

button_add = Button(root, text="+", padx=39, pady=20, command=button_add).grid(row=4, column=1)
button_subtract = Button(root, text=" -", padx=39, pady=20, command=button_subtract).grid(row=4, column=2)
button_multiply = Button(root, text=" *", padx=39, pady=20, command=button_multiply).grid(row=5, column=0)
button_divide = Button(root, text=" /", padx=39, pady=20, command=button_divide).grid(row=5, column=1)
button_modulo = Button(root, text=" % ", padx=35, pady=20, command=button_modulo).grid(row=5, column=2)
button_equal = Button(root, text="= ", padx=85, pady=20, command=calculate).grid(row=6, column=1, columnspan=2)
button_clear = Button(root, text="Clear ", padx=28, pady=20, command=button_clear).grid(row=6, column=0, columnspan=1)
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_number(0)).grid(row=4, column=0)
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_number(1)).grid(row=3, column=0)
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_number(2)).grid(row=3, column=1)
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_number(3)).grid(row=3, column=2)
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_number(4)).grid(row=2, column=0)
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_number(5)).grid(row=2, column=1)
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_number(6)).grid(row=2, column=2)
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_number(7)).grid(row=1, column=0)
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_number(8)).grid(row=1, column=1)
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_number(9)).grid(row=1, column=2)

root.mainloop()

