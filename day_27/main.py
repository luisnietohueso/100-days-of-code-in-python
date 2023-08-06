from tkinter import *

window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=100,pady=100)
# Label
my_label = Label(text='I Am a Label ', font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)


# my_label['text'] = 'New Text'
# my_label.config(text='New text')


# Button

def button_clicked():
    my_label.config(text=f'{input.get()}')


new_button = Button(text='Click Me', command=button_clicked)
new_button.grid(column=0, row=2)
button = Button(text='Click Me', command=button_clicked)
button.grid(column=1, row=1)

# Entry

input = Entry(width=10)
input.grid(column=2, row=3)

window.mainloop()
