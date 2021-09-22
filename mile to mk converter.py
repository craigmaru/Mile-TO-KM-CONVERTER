from tkinter import *


# entry widget
# 4 label widgets
# button saying calculate

def miles_to_km():
    miles = float(user_input.get())
    km = miles * 1.609
    km_result.config(text=f'{int(km)}')


# make a screen 
window = Tk()
window.title('Mile to KM Converter')
# window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# entry widget
user_input = Entry(width=7)
user_input.grid(column=1, row=0)

# miles Label
miles_label = Label(text='Miles', )
miles_label.grid(column=2, row=0)

# is equals label
is_equal_to = Label(text='is equal to')
is_equal_to.grid(column=0, row=1)

# km result starting at 0
km_result = Label(text='0')
km_result.grid(column=1, row=1)

# km label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# calculate
calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)

window.mainloop()
