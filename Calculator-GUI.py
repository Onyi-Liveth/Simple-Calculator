from tkinter import *

view = Tk()                         # Creates a basic window
view.title("Onyi's calculator")
view.resizable(True, True)          # Allows user to resize calculator


# This function continuously updates the input field whenever a user enters
# a number


def click(item):
    global expression
    expression = expression + str(item)
    user_input.set(expression)

# This function calculates the expression


def equal():
    try:
        global expression
        result = str(eval(expression))
        user_input.set(result)
        expression = ''

    except ValueError:
        user_input.set(" error ")
        expression = ""

# This function clears the entire expression


def clear_field():
    global expression
    expression = ''
    user_input.set('')

# This function clears the last input in the expression


def backspace():
    current = input_field.get()
    x = len(current)-1
    input_field.delete(x, END)


expression = " "                     # expression: A string that will be evaluated as python code
user_input = StringVar()             # StringVar is used to hold string

# Frame for the input field


input_frame = Frame(view, bd=0, highlightbackground='black',
                    highlightcolor='black', highlightthickness=2)
input_frame.pack(side=TOP)


# Input field inside the Frame
# Entry() is used to accept single line strings from user

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=user_input,
                    width=50, bg='#eee', bd=0, justify=RIGHT)
input_field.pack(ipady=10)              # Pads widget by 10 pixels vertically
input_field.grid(row=0, column=0, columnspan=4)

# Frame for button field
# Pack() is used to make the widget fill the entire frame

button_frame = Frame(view, width=312, height=272.5, bg='grey')
button_frame.pack()

# First row


clear = (Button(button_frame, text='AC', fg='grey', width=10, height=3, bd=0, bg='#eee',
                cursor='hand2', command=lambda: clear_field()).grid(row=0, column=0, padx=1, pady=1))
divide = (Button(button_frame, text='/', fg='grey', width=10, height=3, bd=0, bg='#eee',
                 cursor='hand2', command=lambda: click('/')).grid(row=0, column=1, padx=1, pady=1))
multiply = (Button(button_frame, text='x', fg='grey', width=10, height=3, bd=0, bg='#eee',
                   cursor='hand2', command=lambda: click('*')).grid(row=0, column=2, padx=1, pady=1))
back_button = (Button(button_frame, text='DEL', fg='grey', width=10, height=3, bd=0, bg='#eee',
                      cursor='hand2', command=lambda: backspace()).grid(row=0, column=3, padx=1, pady=1))

# Second row

seven = (Button(button_frame, text='7', fg='grey', width=10, height=3, bd=0, bg='#eee',
                cursor='hand2', command=lambda: click('7')).grid(row=1, column=0, padx=1, pady=1))
eight = (Button(button_frame, text='8', fg='grey', width=10, height=3, bd=0, bg='#eee',
                cursor='hand2', command=lambda: click('8')).grid(row=1, column=1, padx=1, pady=1))
nine = (Button(button_frame, text='9', fg='grey', width=10, height=3, bd=0, bg='#eee',
               cursor='hand2', command=lambda: click('9')).grid(row=1, column=2, padx=1, pady=1))
subtraction = (Button(button_frame, text='-', fg='grey', width=10, height=3, bd=0, bg='#eee',
                      cursor='hand2', command=lambda: click('-')).grid(row=1, column=3, padx=1, pady=1))

# Third row

four = (Button(button_frame, text='4', fg='grey', width=10, height=3, bd=0, bg='#eee',
               cursor='hand2', command=lambda: click('4')).grid(row=2, column=0, padx=1, pady=1))
five = (Button(button_frame, text='5', fg='grey', width=10, height=3, bd=0, bg='#eee',
               cursor='hand2', command=lambda: click('5')).grid(row=2, column=1, padx=1, pady=1))
six = (Button(button_frame, text='6', fg='grey', width=10, height=3, bd=0, bg='#eee',
              cursor='hand2', command=lambda: click('6')).grid(row=2, column=2, padx=1, pady=1))
add = (Button(button_frame, text='+', fg='grey', width=10, height=3, bd=0, bg='#eee',
              cursor='hand2', command=lambda: click('+')).grid(row=2, column=3, padx=1, pady=1))

# Fourth row

one = (Button(button_frame, text='1', fg='grey', width=10, height=3, bd=0, bg='#eee',
              cursor='hand2', command=lambda: click('1')).grid(row=3, column=0, padx=1, pady=1))
two = (Button(button_frame, text='2', fg='grey', width=10, height=3, bd=0, bg='#eee',
              cursor='hand2', command=lambda: click('2')).grid(row=3, column=1, padx=1, pady=1))
three = (Button(button_frame, text='3', fg='grey', width=10, height=3, bd=0, bg='#eee',
                cursor='hand2', command=lambda: click('3')).grid(row=3, column=2, padx=1, pady=1))
equal_to = (Button(button_frame, text='=', fg='grey', width=10, height=7, bd=0, bg='#eee',
                   cursor='hand2', command=lambda: equal()).grid(row=3, column=3, rowspan=2, padx=1, pady=1))

# Fifth row

percent = (Button(button_frame, text='%', fg='grey', width=10, height=3, bd=0, bg='#eee',
                  cursor='hand2', command=lambda: click('%')).grid(row=4, column=0, padx=1, pady=1))
zero = (Button(button_frame, text='0', fg='grey', width=10, height=3, bd=0, bg='#eee',
               cursor='hand2', command=lambda: click('0')).grid(row=4, column=1, padx=1, pady=1))
decimal_point = (Button(button_frame, text='.', fg='grey', width=10, height=3, bd=0, bg='#eee',
                        cursor='hand2', command=lambda: click('.')).grid(row=4, column=2, padx=1, pady=1))


view.mainloop()
