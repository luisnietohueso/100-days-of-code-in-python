from tkinter import *


def convert_miles_to_km():
    miles = float(box_mile.get())
    km = miles * 1.609
    label_num.config(text=f'{km} (approx)')


window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=250, height=100)
window.config(padx=10, pady=10)

# Component of Miles labels and box
box_mile = Entry(width=10)
box_mile.insert(END, string='0')
box_mile.grid(row=0, column=1)
label_mile = Label(text='Miles')
label_mile.grid(row=0, column=2)

# Component of Kilometres labels
label_equal = Label(text='Is Equal To: ')
label_equal.grid(row=1, column=0)
label_num = Label(text='0')
label_num.grid(row=1, column=1)
label_km = Label(text='Km')
label_km.grid(row=1, column=2)

# Component of Calculate


button = Button(text='Calculate', command=convert_miles_to_km)
button.grid(row=2, column=1)

window.mainloop()
