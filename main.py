import tkinter as tk
from tkinter import messagebox
import pandas as pd
df = pd.read_csv("questions.csv")
print(df.columns)
# print(df)
# row = df.iloc[0]
# print(row["Question"])
# print(row["Correct"])
root = tk.Tk()
root.title("Flash Card")
root.geometry("600x400")


current_index = 0
correct_answers = 0
wrong_answers = 0
def load_question():
    question = df.iloc[current_index]
    question_label.config(text=question["Question"])

    button1.config(text=question["A"], command=lambda: checking_answer(question["A"]))
    button2.config(text=question["B"], command=lambda: checking_answer(question["B"]))
    button3.config(text=question["C"], command=lambda: checking_answer(question["C"]))
    button4.config(text=question["D"], command=lambda: checking_answer(question["D"]))
    score_label.config(text=f"Correct: {correct_answers} Wrong: {wrong_answers}")


def checking_answer(selected_answer):
    global current_index
    global correct_answers
    global wrong_answers
    question = df.iloc[current_index]

    if selected_answer == question["Correct"]:
        messagebox.showinfo("Result", "Correct!")
        correct_answers += 1
    else:
        messagebox.showinfo("Result", "Incorrect!")
        wrong_answers += 1
    current_index += 1

    if current_index < len(df):
        load_question()
    else:
        question_label.config(text="Quiz Finished!")

        button1.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()



title = tk.Label(root, text="Flash Card", font=("Arial", 24, "bold"))
title.pack(pady=10)

score_label = tk.Label(root, text="Correct: 0   Wrong: 0", font=("Arial", 12, "bold"))
score_label.pack(pady=10)

question_label = tk.Label(root, font=("Arial", 16), wraplength=500)
question_label.pack(pady=30)

button_frame = tk.Frame(root)
button_frame.pack()

button1 = tk.Button(button_frame, width=20, height=4)
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = tk.Button(button_frame, width=20, height=4)
button2.grid(row=0, column=1, padx=10, pady=10)

button3 = tk.Button(button_frame, width=20, height=4)
button3.grid(row=1, column=0, padx=10, pady=10)

button4 = tk.Button(button_frame, width=20, height=4)
button4.grid(row=1, column=1, padx=10, pady=10)

load_question()

root.mainloop()