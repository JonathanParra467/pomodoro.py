"""
create a promodoro timer

"""

#!/usr/bin/env python3
"""
Simple Pomodoro timer you can paste into Visual Studio Code.
"""
import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
WORK_MIN = 25        # work session (minutes)
SHORT_BREAK_MIN = 5  # short break (minutes)
LONG_BREAK_MIN = 15  # long break (minutes)
CYLES_BEFORE_LONG = 4

reps = 0
timer = None

# ---------------------------- TIMER RESET ----------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Pomodoro Timer", fg="black")
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % (CYLES_BEFORE_LONG * 2) == 0:
        # Long break
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg="red")
    elif reps % 2 == 0:
        # Short break
        count_down(short_break_sec)
        title_label.config(text="Break", fg="orange")
    else:
        # Work
        count_down(work_sec)
        title_label.config(text="Work", fg="green")

# ---------------------------- COUNTDOWN MECHANISM --------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP -------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg="white")

title_label = tk.Label(text="Pomodoro Timer", fg="black", bg="white", font=("Arial", 35, "bold"))
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg="white", highlightthickness=0)
timer_text = canvas.create_text(100, 112, text="00:00", fill="black", font=("Arial", 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", command=start_timer, font=("Arial", 12))
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", command=reset_timer, font=("Arial", 12))
reset_button.grid(column=2, row=2)

check_marks = tk.Label(fg="green", bg="white", font=("Arial", 20))
check_marks.grid(column=1, row=3)

window.mainloop()
