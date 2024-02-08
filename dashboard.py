import tkinter as tk
from tkinter import messagebox
from create_quiz import CreateQuiz  # Assuming CreateQuiz is correctly set up

def show_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Dashboard")

    tk.Label(dashboard, text="Welcome to the Dashboard!").pack(pady=20)

    # Corrected to open the Create Quiz window
    tk.Button(dashboard, text="Create Quiz", command=open_create_quiz).pack(pady=10)
    tk.Button(dashboard, text="View Quiz Results", command=lambda: messagebox.showinfo("Action", "View Results")).pack(pady=10)

    dashboard.mainloop()

def open_create_quiz():
    # This standalone function correctly opens the Create Quiz window
    create_quiz_window = tk.Toplevel()  # No need for 'self' in a standalone function
    create_quiz = CreateQuiz(create_quiz_window)  
    
if __name__ == "__main__":
    show_dashboard()
