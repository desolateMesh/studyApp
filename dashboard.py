import tkinter as tk
from tkinter import messagebox
from create_quiz import CreateQuiz

def show_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Dashboard")

    tk.Label(dashboard, text="Welcome to the Dashboard!").pack(pady=20)

    tk.Button(dashboard, text="Create Questions", command=open_create_quiz).pack(pady=10)
    tk.Button(dashboard, text="View Quiz Results", command=lambda: messagebox.showinfo("Action", "View Results")).pack(pady=10)
    tk.Button(dashboard, text="View Questions", command=open_viewQuestionScreen).pack(pady=10)

    dashboard.mainloop()

def open_create_quiz():
    create_quiz_window = tk.Toplevel()  
    create_quiz = CreateQuiz(create_quiz_window)  

def open_viewQuestionScreen():
    viewQuestionScreen = tk.Tk()
    viewQuestionScreen.title("Quiz Questions")
    
if __name__ == "__main__":
    show_dashboard()
