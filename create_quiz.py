import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


class CreateQuiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Create Quiz Questions")

       
        tk.Label(self.master, text="Quiz ID:").grid(row=0, column=0, sticky="w")
        self.quiz_title = tk.Entry(self.master)
        self.quiz_title.grid(row=0, column=1, sticky="ew")

        tk.Label(self.master, text="Category:").grid(row=1, column=0, sticky="w")
        self.quiz_category = tk.Entry(self.master)
        self.quiz_category.grid(row=1, column=1, sticky="ew")

       
        tk.Label(self.master, text="Question:").grid(row=2, column=0, sticky="w")
        self.question_text = tk.Entry(self.master)
        self.question_text.grid(row=2, column=1, sticky="ew")

        tk.Label(self.master, text="Correct Answer:").grid(row=3, column=0, sticky="w")
        self.correct_answer = tk.Entry(self.master)
        self.correct_answer.grid(row=3, column=1, sticky="ew")

        tk.Label(self.master, text="A):").grid(row=4, column=0, sticky="w")
        self.answer_a = tk.Entry(self.master)
        self.answer_a.grid(row=4, column=1, sticky="ew")

        tk.Label(self.master, text="B):").grid(row=5, column=0, sticky="w")
        self.answer_b = tk.Entry(self.master)
        self.answer_b.grid(row=5, column=1, sticky="ew")

        tk.Label(self.master, text="C):").grid(row=6, column=0, sticky="w")
        self.answer_c = tk.Entry(self.master)
        self.answer_c.grid(row=6, column=1, sticky="ew")

        tk.Label(self.master, text="D):").grid(row=7, column=0, sticky="w")
        self.answer_d = tk.Entry(self.master)
        self.answer_d.grid(row=7, column=1, sticky="ew")

        tk.Button(self.master, text="Save Quiz", command=self.save_quiz).grid(row=8, column=0, columnspan=2)

        self.master.grid_columnconfigure(1, weight=1)  

    def save_quiz(self):
        user_id = 1  
        category = self.quiz_category.get()
        question_text = self.question_text.get()
        correct_answer = self.correct_answer.get()
        answer_a = self.answer_a.get()
        answer_b = self.answer_b.get()
        answer_c = self.answer_c.get()
        answer_d = self.answer_d.get()

        conn = sqlite3.connect('quiz_application.db')
        c = conn.cursor()

        c.execute("INSERT INTO quizzes (user_id, category, number_of_questions) VALUES (?, ?, ?)", 
                (user_id, category, 1))  
        quiz_id = c.lastrowid  
        c.execute("""INSERT INTO questions (quiz_id, question_text, correct_answer, answer_a, answer_b, answer_c, answer_d)
                    VALUES (?, ?, ?, ?, ?, ?, ?)""", 
                (quiz_id, question_text, correct_answer, answer_a, answer_b, answer_c, answer_d))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Quiz and question saved successfully!")

    def open_create_quiz():
        try:
            create_quiz_window = tk.Toplevel()
            create_quiz_app = CreateQuiz(create_quiz_window)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Create Quiz window: {e}")


def main():
    root = tk.Tk()
    app = CreateQuiz(root)
    root.mainloop()

if __name__ == "__main__":
    main()
