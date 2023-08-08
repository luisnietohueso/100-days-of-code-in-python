from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetition = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global repetition, timer
    window.after_cancel(timer)
    canvas.itemconfigure(canvas_timer, text='25:00')
    label_timer.config(text='Timer', font=(FONT_NAME, 35, 'bold'), bg=YELLOW)
    label_tick.config(text='')
    repetition = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repetition
    repetition += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if repetition % 2 == 1:
        label_timer.config(text='Work', font=(FONT_NAME, 35, 'bold'), bg=GREEN)
        count_down(work_sec)
    elif repetition % 2 == 0:
        label_timer.config(text='Break', font=(FONT_NAME, 35, 'bold'), bg=PINK)
        count_down(short_break_sec)
    elif repetition == 8:
        label_timer.config(text='Break', font=(FONT_NAME, 35, 'bold'), bg=RED)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfigure(canvas_timer, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(repetition / 2)
        for _ in range(work_sessions):
            marks += '/'
        label_tick.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
window.after(1000, )
# Labels I need
label_timer = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), bg=YELLOW)
label_timer.grid(row=0, column=1)

label_tick = Label(font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
label_tick.grid(row=3, column=1)
# Canvas I need
canvas = Canvas(width=200, height=226, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png', )
canvas.create_image(100, 112, image=tomato_img)
canvas_timer = canvas.create_text(103, 130, text='25:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

# Buttons I need
button_star = Button(text='Star', command=start_timer)
button_star.grid(row=2, column=0)
button_reset = Button(text='Reset', command=reset_timer)
button_reset.grid(row=2, column=2)

window.mainloop()
