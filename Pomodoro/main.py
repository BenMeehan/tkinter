import tkinter as tk

TICK = '✔'
rep = 0
WORK_TIME = 25
SHORT_BREAK = 5
LONG_BREAK = 20
after_holder = None


def reset_fn():
    heading.config(text='Timer', fg='green')
    checkmark.config(text='')
    rep = 0
    canvas.itemconfig(canvas_text, text=f"00:00")
    window.after_cancel(after_holder)


def start_fn():
    global rep
    if rep % 2 == 0:
        heading.config(text="Work", fg='red')
        counter(WORK_TIME*60)
    else:
        heading.config(text="Break", fg='gold')
        counter(SHORT_BREAK*60)


def counter(count):
    global rep, TICK
    mins = count//60
    secs = count % 60
    if(mins <= 9):
        mins = f'0{mins}'
    if(secs <= 9):
        secs = f'0{secs}'
    canvas.itemconfig(canvas_text, text=f"{mins}:{secs}")
    if count > 0:
        global after_holder
        after_holder = window.after(1000, counter, count-1)
    else:
        if rep == 7:
            heading.config(text="Long Break", fg='blue')
            TICK = "✔✔✔✔"
            checkmark.config(text=TICK)
            counter(LONG_BREAK*60)
            rep += 1
        if(rep <= 6):
            if rep % 2 != 0:
                TICK = '✔'
                for i in range(rep//2):
                    TICK += '✔'
                checkmark.config(text=TICK)
            rep += 1
            start_fn()


window = tk.Tk()
window.title('Pomodoro')
window.config(padx=30, pady=20)

heading = tk.Label(text="Timer", fg="green",
                   font=('Times New Roman', 70, 'bold'))
heading.grid(row=0, column=1)

canvas = tk.Canvas(width=512, height=512)
tomato = tk.PhotoImage(file='./tomato.png')
canvas.create_image(256, 256, image=tomato)
canvas_text = canvas.create_text(270, 340, text="00:00", fill="white",
                                 font=('Arial', 50, 'bold'))
canvas.grid(row=1, column=1)

start = tk.Button(text="start", font=('Arial', 15, 'normal'), command=start_fn)
start.grid(row=2, column=0)

reset = tk.Button(text="reset", font=('Arial', 15, 'normal'), command=reset_fn)
reset.grid(row=2, column=2)

checkmark = tk.Label(text="", fg="green",
                     font=('Times New Roman', 20, 'bold'))
checkmark.grid(row=3, column=1)

window.mainloop()
