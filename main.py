from tkinter import *
from style import  *
# text
button1Text = 'Botão 1'
button2Text = 'Botão 2'

# COLORS


# pack - throws the widget in the nearest position possible in the direction (side) you choose
# grid - griding your widget into positions with column and rows indexes
# place - locates your widget at the given pixel point (ex: 0,0 - top left)

rootWindow = Tk()
rootWindow.geometry('640x320')

# frameCenter = Frame(rootWindow, bg='#888888')
# frameCenter.pack(side=TOP, expand=YES, fill=BOTH)
result_frame = Frame(rootWindow, bg='#1f1f1f')
result_frame.pack(side=TOP, expand=YES, fill=BOTH)

keypad_frame = Frame(rootWindow, bg='#000000')
keypad_frame.pack(side=BOTTOM, expand=YES, fill=BOTH)

result_screen = Label(result_frame, text='', **result_screen_style)
result_screen.pack()

num = 10
for i in range(3):
    for j in reversed(range(3)):
        num = num - 1
        print(i, j, num)
        btn_num = Button(keypad_frame, text=num, **button_style)
        btn_num.grid(row=i, column=j)

btn_num_zero = Button(keypad_frame, text=0, **button_style)
btn_num_zero.grid(row=3, column=1)

btn_clear = Button(keypad_frame, text='C', **button_style)
btn_clear.grid(row=3, column=0)

btn_equal = Button(keypad_frame, text='=', **button_style)
btn_equal.grid(row=3, column=2)

btn_num_divide = Button(keypad_frame, text='/', **button_style)
btn_num_divide.grid(row=0, column=3)

btn_multiply = Button(keypad_frame, text='*', **button_style)
btn_multiply.grid(row=1, column=3)

btn_subtract = Button(keypad_frame, text='-', **button_style)
btn_subtract.grid(row=2, column=3)

btn_plus = Button(keypad_frame, text='+', **button_style)
btn_plus.grid(row=3, column=3)


# functionality

def update_result_screen(clicked_button):
    current_text = str(result_screen.cget('text'))
    updated_text = current_text + str(clicked_button.cget('text'))
    result_screen.configure(text=updated_text)

for widget in keypad_frame.winfo_children():
    widget_text = widget.cget('text')
    if type(widget_text) == int or widget_text in ['+', '-', '*', '/']:
        widget.configure(command = lambda widget = widget : update_result_screen(widget))


def clean_screen():
    result_screen.configure(text='')


btn_clear.configure(command=clean_screen)


def calculation():
    screen_text = result_screen.cget('text')
    result = None
    if '-' in screen_text:
        first_num = int(screen_text.split('-')[0])
        second_num = int(screen_text.split('-')[-1])
        result = first_num - second_num
    if '+' in screen_text:
        first_num = int(screen_text.split('+')[0])
        second_num = int(screen_text.split('+')[-1])
        result = first_num - second_num
    if '*' in screen_text:
        first_num = int(screen_text.split('*')[0])
        second_num = int(screen_text.split('*')[-1])
        result = first_num * second_num
    if '/' in screen_text:
        first_num = int(screen_text.split('/')[0])
        second_num = int(screen_text.split('/')[-1])
        result = first_num / second_num

    result_screen.configure(text=result)


btn_equal.configure(command=calculation)

# end
rootWindow.mainloop()