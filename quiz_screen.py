import tkinter as tk
from tkinter import ttk
import sqlite3

class QuizScreen:
    def __init__(self, master, questions, category):
        self.master = master
        self.questions = questions
        self.category = category
        self.current_question_index = 0 

        self.question_frame = tk.Frame(self.master)
        self.question_frame.pack(pady=10)

        self.master.title(f"Quiz on {self.category}")

        self.question_text = tk.Label(self.question_frame, text="Question will go here", wraplength=400)
        self.question_text.pack()

        
        self.answers_frame = tk.Frame(self.master)
        self.answers_frame.pack(pady=10)

        
        self.var_a = tk.StringVar(value="A. Choice One")
        self.var_b = tk.StringVar(value="B. Choice Two")
        self.var_c = tk.StringVar(value="C. Choice Three")
        self.var_d = tk.StringVar(value="D. Choice Four")

        
        self.radio_a = tk.Radiobutton(self.answers_frame, textvariable=self.var_a, value="A")
        self.radio_a.pack(anchor="w")

        self.radio_b = tk.Radiobutton(self.answers_frame, textvariable=self.var_b, value="B")
        self.radio_b.pack(anchor="w")

        self.radio_c = tk.Radiobutton(self.answers_frame, textvariable=self.var_c, value="C")
        self.radio_c.pack(anchor="w")

        self.radio_d = tk.Radiobutton(self.answers_frame, textvariable=self.var_d, value="D")
        self.radio_d.pack(anchor="w")

      
        self.navigation_frame = tk.Frame(self.master)
        self.navigation_frame.pack(pady=20)

        self.prev_button = tk.Button(self.navigation_frame, text="Previous", command=self.prev_question)
        self.prev_button.grid(row=0, column=0, padx=10)

        self.next_button = tk.Button(self.navigation_frame, text="Next", command=self.next_question)
        self.next_button.grid(row=0, column=1, padx=10)

        self.submit_button = tk.Button(self.navigation_frame, text="Submit", command=self.submit_quiz)
        self.submit_button.grid(row=0, column=2, padx=10)

    def update_question_and_answers(self):
        if self.questions and 0 <= self.current_question_index < len(self.questions):
            current_question = self.questions[self.current_question_index]
            
            self.question_text.config(text=current_question[1])  
            self.var_a.set(f"A. {current_question[3]}")  
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
        
        pass
