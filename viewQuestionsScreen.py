import tkinter as tk
from tkinter import ttk
import sqlite3

class ViewQuestionScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("View Questions")

        self.tree = ttk.Treeview(self.master, columns=('ID', 'Category', 'Question', 'Correct Answer', 'A', 'B', 'C', 'D'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Category', text='Category')
        self.tree.heading('Question', text='Question')
        self.tree.heading('Correct Answer', text='Correct Answer')
        self.tree.heading('A', text='A')
        self.tree.heading('B', text='B')
        self.tree.heading('C', text='C')
        self.tree.heading('D', text='D')
        self.tree.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)


        self.load_questions()

    def load_questions(self):
        conn = sqlite3.connect('quiz_application.db')
        c = conn.cursor()
        query = """SELECT id, quiz_id, question_text, correct_answer, answer_a, answer_b, answer_c, answer_d
               FROM questions"""
        c.execute(query)
        for row in c.fetchall():
            self.tree.insert('', tk.END, values=row)
        conn.close()