import tkinter as tk
from tkinter import messagebox
import sqlite3

class QuizScreen:
    def __init__(self, master, questions, category):
        self.master = master
        self.questions = questions
        self.category = category
        self.current_question_index = 0

        self.master.title(f"Quiz on {self.category}")

        self.question_frame = tk.Frame(self.master)
        self.question_frame.pack(pady=10)

        self.question_text = tk.Label(self.question_frame, text="", wraplength=400)
        self.question_text.pack()

        self.answers_frame = tk.Frame(self.master)
        self.answers_frame.pack(pady=10)

        self.var_a = tk.StringVar()
        self.var_b = tk.StringVar()
        self.var_c = tk.StringVar()
        self.var_d = tk.StringVar()

        self.radio_a = tk.Radiobutton(self.answers_frame, textvariable=self.var_a, value="A", variable=self.var_a)
        self.radio_a.pack(anchor="w")

        self.radio_b = tk.Radiobutton(self.answers_frame, textvariable=self.var_b, value="B", variable=self.var_b)
        self.radio_b.pack(anchor="w")

        self.radio_c = tk.Radiobutton(self.answers_frame, textvariable=self.var_c, value="C", variable=self.var_c)
        self.radio_c.pack(anchor="w")

        self.radio_d = tk.Radiobutton(self.answers_frame, textvariable=self.var_d, value="D", variable=self.var_d)
        self.radio_d.pack(anchor="w")

        self.navigation_frame = tk.Frame(self.master)
        self.navigation_frame.pack(pady=20)

        self.prev_button = tk.Button(self.navigation_frame, text="Previous", command=self.prev_question)
        self.prev_button.grid(row=0, column=0, padx=10)

        self.next_button = tk.Button(self.navigation_frame, text="Next", command=self.next_question)
        self.next_button.grid(row=0, column=1, padx=10)

        self.submit_button = tk.Button(self.navigation_frame, text="Submit", command=self.submit_quiz)
        self.submit_button.grid(row=0, column=2, padx=10)

        # Update the UI with the first question
        self.update_question_and_answers()

    def update_question_and_answers(self):
        if self.questions and 0 <= self.current_question_index < len(self.questions):
            current_question = self.questions[self.current_question_index]
            
            self.question_text.config(text=current_question[1])  # Update question text
            self.var_a.set(f"A. {current_question[3]}")  # Update answer choices
            self.var_b.set(f"B. {current_question[4]}")
            self.var_c.set(f"C. {current_question[5]}")
            self.var_d.set(f"D. {current_question[6]}")
        else:
            self.question_text.config(text="No more questions available.")
            self.var_a.set("A.")
            self.var_b.set("B.")
            self.var_c.set("C.")
            self.var_d.set("D.")

    def prev_question(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.update_question_and_answers()

    def next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.update_question_and_answers()

    def submit_quiz(self):
        # Placeholder for submission logic
        messagebox.showinfo("Quiz Completed", "You have completed the quiz.")
