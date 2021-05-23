from tkinter import *
from functions import metric_to_imperial, converted_difference

#key down function
def click():
    entered_text=text_entry.get()  # will store the value in text_entry into variable entered_text
    output.delete(0.0 ,END)  # clear text box
    answer = metric_to_imperial(entered_text)  # run entered value through function
    output.insert(END, answer) # display answer in 'output' text box
    difference.delete(0.0 ,END)  # clear text box
    difference.insert(END, converted_difference(entered_text))  # display answer in 'difference' text box

# set up window
window = Tk()
window.title("Metric to Imperial Converter")
window.configure(background="white")
window.geometry("500x200")

# add label
Label(window, text = "Enter a value in mm to convert to imperial:", bg ="white", fg="black", font="none 14 bold").grid(row=1, column=0, sticky=W)

# add text entry box
text_entry = Entry(window, width=20, bg="white")
text_entry.grid(row=2, column=0, sticky=W)

# add submit button
Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0, sticky=W)

# add a second label
Label(window, text = "Closest imperial value:", bg ="white", fg="black", font="none 14 bold").grid(row=4, column=0, sticky=W)

# add a text box for output
output = Text(window, width=20, height=1, wrap=WORD, background="white")
output.grid(row=5, column=0, sticky=W)

# add a third label
Label(window, text = "Difference between input and converted value is:", bg ="white", fg="black", font="none 14 bold").grid(row=6, column=0, sticky=W)

# add a text box for converted difference
difference = Text(window, width=20, height=1, wrap=WORD, background="white")
difference.grid(row=7, column=0, sticky=W)

# run the program
window.mainloop()