import tkinter as tk

grams = 0


def convert():
    mg = int(entry.get())
    grams = mg/1000
    label['text'] = f"milli-grams is equal to \t{grams}\t grams"


window = tk.Tk()
window.title("milli-grams to grams")
window.minsize(400, 100)
window.config(padx=20, pady=20)

# Entry
entry = tk.Entry()
entry.grid(row=0, column=0)
entry.focus()

# Label
label = tk.Label(text=f"milli-grams is equal to \t{grams}\t grams")
label.grid(row=0, column=1)
label.config(padx=10, pady=10)

# Button
button = tk.Button(text="convert", command=convert)
button.grid(row=1, column=1)
button.config()

window.mainloop()
