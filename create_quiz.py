import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


class CreateQuiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Create Quiz")

        # Quiz Details Section
        tk.Label(self.master, text="Quiz Title:").grid(row=0, column=0, sticky="w")
        self.quiz_title = tk.Entry(self.master)
        self.quiz_title.grid(row=0, column=1, sticky="ew")

        tk.Label(self.master, text="Category:").grid(row=1, column=0, sticky="w")
        self.quiz_category = tk.Entry(self.master)
        self.quiz_category.grid(row=1, column=1, sticky="ew")

        # Questions Section
        tk.Label(self.master, text="Question:").grid(row=2, column=0, sticky="w")
        self.question_text = tk.Entry(self.master)
        self.question_text.grid(row=2, column=1, sticky="ew")

        tk.Label(self.master, text="Correct Answer:").grid(row=3, column=0, sticky="w")
        self.correct_answer = tk.Entry(self.master)
        self.correct_answer.grid(row=3, column=1, sticky="ew")

        # Placeholder for multiple choice answers
        # You can add more entries for additional answers

        # Save Button
        tk.Button(self.master, text="Save Quiz", command=self.save_quiz).grid(row=4, column=0, columnspan=2)

        self.master.grid_columnconfigure(1, weight=1)  # Make the entry fields expand to fill the dialog

    def save_quiz(self):
        title = self.quiz_title.get()
        category = self.quiz_category.get()
        question = self.question_text.get()
        correct_answer = self.correct_answer.get()
        print(title, category, question, correct_answer)  

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
