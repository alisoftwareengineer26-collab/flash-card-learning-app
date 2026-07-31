import tkinter as tk
import pandas as pd
import random

df = pd.read_csv("questions.csv")
shuffled_questions = df.sample(frac=1).reset_index(drop=True)
root = tk.Tk()
root.title("Flash Card")
root.geometry("600x450")

current_index = 0
correct_answers = 0
wrong_answers = 0

def load_question():
    question = shuffled_questions.iloc[current_index]
    # quantity_questions = (len(question) + 1)
    for button in buttons:
        button.config(state="normal")
    question_label.config(text=question["Question"])
    answer_columns = ["A", "B", "C", "D"]
    random.shuffle(answer_columns)
    for index, column in enumerate(answer_columns):
        buttons[index].config(
            text=question[column],
            command=lambda answer=question[column], button=buttons[index]:
            checking_answer(answer, button))

    total_label.config(text=f"Question: {current_index + 1}/{len(shuffled_questions)}")

    score_label.config(
        text=f"Correct: {correct_answers} Wrong: {wrong_answers}")

    accuracy_label.config(text=f"Accuracy: {accuracy():.0f}%")

def checking_answer(selected_answer, clicked_button):
    global current_index
    global correct_answers
    global wrong_answers

    for button in buttons:
        button.config(state="disabled")

    question = shuffled_questions.iloc[current_index]

    if selected_answer == question["Correct"]:
        clicked_button.config(bg="green")
        correct_answers += 1
    else:
        clicked_button.config(bg="red")
        wrong_answers += 1
        for button in buttons:
            if button["text"] == question["Correct"]:
                button.config(bg="green")
                break

    score_label.config(text=f"Correct: {correct_answers} Wrong: {wrong_answers}")

    accuracy_label.config(text=f"Accuracy: {accuracy():.0f}%")

    root.after(1000, next_question)

def next_question():
    global current_index

    current_index += 1

    if current_index < len(shuffled_questions):
        for button in buttons:
            button.config(bg="SystemButtonFace")

        load_question()

    else:
        question_label.config(text="Quiz Finished!")
        for button in buttons:
            button.destroy()

def accuracy():
    if current_index == 0:
        return 0
    else:
        answered = correct_answers + wrong_answers
        return (correct_answers / answered) * 100

total_label= tk.Label(root, text="", font=("Times New Roman", 20, "bold"))
total_label.pack(pady=10)

score_label = tk.Label(root, text="Correct: 0   Wrong: 0", font=("Arial", 12, "bold"))
score_label.pack(pady=10)

accuracy_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
accuracy_label.pack(pady=2)

question_label = tk.Label(root, font=("Arial", 16), wraplength=500)
question_label.pack(pady=30)

button_frame = tk.Frame(root)
button_frame.pack()
buttons = []
for i in range(4):
    button = tk.Button(button_frame, width=20, height=4)
    buttons.append(button)
    buttons[i].grid(
        row=i //2,
        column = i%2,
        padx=10, pady=10
    )

load_question()
root.mainloop()