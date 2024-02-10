import tkinter as tk
from tkinter import ttk, messagebox
from create_quiz import CreateQuiz
from viewQuestionsScreen import ViewQuestionScreen
from quiz_screen import QuizScreen
import sqlite3

def show_dashboard():
    dashboard = tk.Tk()
    dashboard.title("User Dashboard")
    dashboard.geometry("500x300")

    tk.Label(dashboard, text="Welcome to the Dashboard!", font=('Helvetica', 16)).pack(pady=20)

    left_frame = tk.Frame(dashboard)
    left_frame.pack(side=tk.LEFT, fill='y', padx=10)

    right_frame = tk.Frame(dashboard)
    right_frame.pack(side=tk.RIGHT, fill='both', expand=True, padx=10)

    tk.Button(left_frame, text="Create Questions", command=open_create_quiz_questions).pack(pady=5)
    tk.Button(left_frame, text="View Questions", command=lambda: open_viewQuestionScreen(dashboard)).pack(pady=5)
    tk.Button(left_frame, text="Generate Quiz", command=lambda: generate_quiz(selected_category.get())).pack(pady=5)
    tk.Button(left_frame, text="View Quiz Results", command=open_view_results).pack(pady=5)

    categories = fetch_categories()  

    tk.Label(right_frame, text="Select Category:").grid(row=0, column=0, sticky='w')
    selected_category = tk.StringVar()
    category_dropdown = ttk.Combobox(right_frame, textvariable=selected_category, values=categories)
    category_dropdown.grid(row=0, column=1, sticky='ew', pady=2)
    category_dropdown.current(0)  

    tk.Label(right_frame, text="Number of Questions:").grid(row=1, column=0, sticky='w', pady=2)
    question_count = tk.Spinbox(right_frame, from_=1, to=20, width=5)
    question_count.grid(row=1, column=1, sticky='w')

    dashboard.mainloop()

def open_create_quiz_questions():
    create_quiz_window = tk.Toplevel()  
    create_quiz_app = CreateQuiz(create_quiz_window)

def open_viewQuestionScreen(master):
    view_question_window = tk.Toplevel(master)  
    view_screen = ViewQuestionScreen(view_question_window)

def fetch_categories():
    conn = sqlite3.connect('quiz_application.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT category FROM quizzes")
    categories = [row[0] for row in c.fetchall()]
    conn.close()
    return categories

categories = fetch_categories()

def open_view_results():
    messagebox.showinfo("View Results", "Results viewing not implemented yet.")

def generate_quiz(category):
    conn = sqlite3.connect('quiz_application.db')
    c = conn.cursor()
    query = """SELECT id, question_text, correct_answer, answer_a, answer_b, answer_c, answer_d
               FROM questions WHERE category=?"""
    c.execute(query, (category,))
    questions = c.fetchall()
    conn.close()

    if questions:
        # Pass these questions to the QuizScreen
        quiz_window = tk.Toplevel()
        quiz_screen = QuizScreen(quiz_window, questions, category)
    else:
        messagebox.showinfo("Generate Quiz", "No questions found for the selected category.")




if __name__ == "__main__":
    show_dashboard()
