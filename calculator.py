from tkinter import *
from functools import partial
from calculate import *
from tkinter import Tk

# Generate the main computer interface
def overall_arrangement(root):
    menu = Menu(root)  # Menu
    submenu1 = Menu(menu, tearoff=0)  # Divided into Windows, 0 is in the original window, 1 is clicked into two Windows
    menu.add_cascade(label='EDIT', menu=submenu1)  # Add suboptions (the label argument is what is displayed)
    submenu1.add_command(label='COPY', command=lambda: edit(entry, 'copy'))  # Add command
    submenu1.add_command(label='CUT', command=lambda: edit(entry, 'cut'))
    submenu1.add_command(label='PASTE', command=lambda: edit(entry, 'paste'))
    submenu2 = Menu(menu, tearoff=0)
    menu.add_cascade(label='VIEW', menu=submenu2)
    submenu2.add_command(label='HELP', command=lambda: view(entry, 'help'))
    submenu2.add_command(label='AUTHOR', command=lambda: view(entry, 'author'))
    root.config(menu=menu)  # Reconfigure and add a menu

    label = Label(root, width=40, height=1, bd=5, bg='#cde9ff', anchor='se',
                  textvariable=label_text)  # Tags that can display text or pictures
    label.grid(row=0, columnspan=5)  # A layout that registers and displays controls to a window; rowspan: Sets the number of columns that a cell spans vertically

    entry = Entry(root, width=40, bd=5, bg='#cde9ff', justify="right", font=('Arial', 12))  # Text box (single line)
    entry.grid(row=1, column=0, columnspan=5, sticky=N + W + S + E, padx=5, pady=5)  # Set the size of the x - and y-direction blank space around the control



    myButton = partial(Button, root, width=5, cursor='hand2', activebackground='#cde9ff')  # Partial function: A function with fixed parameters
    


    button_backspace = myButton(text='←', command=lambda: backspace(entry))  # command specifies the callback function for the button message
    button_clear = myButton(text=' C ', command=lambda: clear(entry))
    button_left_parenthesis = myButton(text='(', command=lambda: get_input(entry, '('))
    button_right_parenthesis = myButton(text=')', command=lambda: get_input(entry, ')'))
    button_root = myButton(text='√x', command=lambda: get_input(entry, '√('))
    button_clear.grid(row=2, column=0)
    button_backspace.grid(row=2, column=1)
    button_left_parenthesis.grid(row=2, column=2)
    button_right_parenthesis.grid(row=2, column=3)
    button_root.grid(row=3, column=4)



    button_sin = myButton(text='sin', command=lambda: get_input(entry, 'sin('))  # button
    button_arcsin = myButton(text='arcsin', command=lambda: get_input(entry, 'arcsin('))
    button_exp = myButton(text='e', command=lambda: get_input(entry, 'e'))
    button_ln = myButton(text='ln', command=lambda: get_input(entry, 'ln('))
    button_xy = myButton(text='x^y', command=lambda: get_input(entry, '^'))
    button_arcsin.grid(row=3, column=0)
    button_sin.grid(row=3, column=1)
    button_exp.grid(row=3, column=2)
    button_ln.grid(row=3, column=3)
    button_xy.grid(row=2, column=4)


    button_1 = myButton(text=' 1 ', command=lambda: get_input(entry, '1'))
    button_2 = myButton(text=' 2 ', command=lambda: get_input(entry, '2'))
    button_3 = myButton(text=' 3 ', command=lambda: get_input(entry, '3'))
    button_subtract = myButton(text=' - ', command=lambda: get_input(entry, '-'))
    button_equal = myButton(text=' \n = \n ', command=lambda: calculator(entry))
    button_1.grid(row=6, column=0)
    button_2.grid(row=6, column=1)
    button_3.grid(row=6, column=2)
    button_subtract.grid(row=6, column=3)
    button_equal.grid(row=6, column=4, rowspan=2)


    button_4 = myButton(text=' 4 ', command=lambda: get_input(entry, '4'))
    button_5 = myButton(text=' 5 ', command=lambda: get_input(entry, '5'))
    button_6 = myButton(text=' 6 ', command=lambda: get_input(entry, '6'))
    button_multiply = myButton(text=' * ', command=lambda: get_input(entry, '*'))
    button_factorial = myButton(text='factorial', command=lambda: factorial(entry))
    button_4.grid(row=5, column=0)
    button_5.grid(row=5, column=1)
    button_6.grid(row=5, column=2)
    button_multiply.grid(row=5, column=3)
    button_factorial.grid(row=5, column=4)


    button_7 = myButton(text=' 7 ', command=lambda: get_input(entry, '7'))
    button_8 = myButton(text=' 8 ', command=lambda: get_input(entry, '8'))
    button_9 = myButton(text=' 9 ', command=lambda: get_input(entry, '9'))
    button_divide = myButton(text=' / ', command=lambda: get_input(entry, '/'))
    button_precent = myButton(text='%', command=lambda: get_input(entry, '%'))
    button_7.grid(row=4, column=0)
    button_8.grid(row=4, column=1)
    button_9.grid(row=4, column=2)
    button_divide.grid(row=4, column=3)
    button_precent.grid(row=4, column=4)

      

    button_π = myButton(text=' π ', command=lambda: get_input(entry, 'π'))
    button_0 = myButton(text=' 0 ', command=lambda: get_input(entry, '0'))
    button_decimal_point = myButton(text=' . ', command=lambda: get_input(entry, '.'))
    button_plus = myButton(text=' + ', command=lambda: get_input(entry, '+'))
    button_π.grid(row=7, column=0)
    button_0.grid(row=7, column=1)
    button_decimal_point.grid(row=7, column=2)
    button_plus.grid(row=7, column=3)

    # rowspan：Sets the number of rows that the cell spans horizontally


# Copy, cut, or paste a formula or answer in a text box
def edit(entry, argu):
    """
    :param entry: textbox
    :param argu: the value corresponding to the button
    """
    if argu == 'copy':
        entry.event_generate("<<Copy>>")
    elif argu == 'cut':
        entry.event_generate("<<Cut>>")
        clear(entry)
    elif argu == 'paste':
        entry.event_generate("<<Paste>>")




# See usage help and author information
def view(entry, argu):
    root = Tk()
    root.resizable(0, 0)
    text = Text(root, width=20, height=2, bd=5, bg='#66ccff', font=('Arial', 12))
    text.grid(padx=5, pady=5)
    if argu == 'help':
        root.title('HELP')
        text.insert(INSERT, 'press the formula and number button \n')
        text.insert(INSERT, 'press the equal sign button')
    elif argu == 'author':
        root.title('AUTHOR')
        text.insert(INSERT, 'Author: Yongkang Chen and Zhexuan Wang  \n')
        text.insert(INSERT, 'Time: 2023-01-29')


# Delete the last input
def backspace(entry):
    entry.delete(len(entry.get()) - 1)  # Deletes the last input value in the text box


# Delete all input and display content
def clear(entry):
    entry.delete(0, END)  # Delete all the contents of the text box
    label_text.set('')


# Click the calculator Input button to add content to the text box
def get_input(entry, argu):
    formula = entry.get()
    for char in formula:
        if '\u4e00' <= char <= '\u9fa5':
            clear(entry)
    entry.insert(INSERT, argu)


# Decimal integers are converted to binary integers
def factorial(entry):
    try:
        formula = entry.get()
        if re.match('\d+$', formula):
            number = int(formula)
            storage = []  # The remainder of each time you divide by 2
            result = ''
            while number:
                storage.append(number % 2)
                number //= 2  # Integer division, returns quotient
            while storage:
                result += str(storage.pop())  # Invert all the remainder to get the result
            clear(entry)
            entry.insert(END, result)
            label_text.set(''.join(formula + '='))
        else:
            clear(entry)
            entry.insert(END, 'ERROR')
    except:
        clear(entry)
        entry.insert(END, 'ERROR')


# Click "=" to calculate
def calculator(entry):
    try:
        formula = entry.get()
        # If the input content is only a number, π, or e, the content is still displayed
        if re.match('-?[\d+,π,e]\.?\d*$', formula):
            label_text.set(''.join(formula + '='))
            return
        # If the input content is a formula, the calculation result is displayed
        result = final_calc(formula_format(formula))
        clear(entry)
        entry.insert(END, result)  # Output the result to a text box
        label_text.set(''.join(formula + '='))
    except:
        clear(entry)
        entry.insert(END, 'ERROR')




if __name__ == '__main__':
    root = Tk()  # Build window
    root.title('CALCULATOR')  # Window name
    root.resizable(0, 0)  # The window size is adjustable, indicating the variability of x and y directions respectively
    global label_text
    label_text = StringVar()
    overall_arrangement(root)
    root.mainloop()

