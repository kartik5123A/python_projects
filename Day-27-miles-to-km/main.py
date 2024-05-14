import tkinter

window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(width = 250, height = 120)
window.config(padx = 20, pady = 20)

# input
input = tkinter.Entry(width = 12)
input.grid(row = 0, column = 1)

# calculation
def calculate():
    kilo_meter = float(input.get())*1.609344
    # label(calculate)
    label_4 = tkinter.Label(text = f"{round(kilo_meter, 2)}", font = ("Arial", 12, "bold"))
    label_4.grid(row = 1, column = 1)

# label(Miles)
label_1 = tkinter.Label(text = "Miles", font = ("Arial", 12, "bold"))
label_1.grid(row = 0, column = 2)

# label(is equal to)
label_2 = tkinter.Label(text = "is equal to", font = ("Arial", 12, "bold"))
label_2.grid(row = 1, column = 0)

# label(Km)
label_3 = tkinter.Label(text = "Km", font = ("Arial", 12, "bold"))
label_3.grid(row = 1, column = 2)

# button
button = tkinter.Button(text = "Calculate", command = calculate)
button.grid(row = 2, column = 1)

window.mainloop()