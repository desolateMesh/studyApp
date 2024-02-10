import tkinter as tk
from tkinter import messagebox
import sqlite3
from create_quiz import CreateQuiz
from viewQuestionsScreen import ViewQuestionScreen
from quiz_screen import QuizScreen
from dashboard import show_dashboard

def login_user(username, password):
    conn = sqlite3.connect('quiz_application.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    account = c.fetchone()
    conn.close()
    
    if account:
        messagebox.showinfo("Login Success", "You have successfully logged in!")
        root.destroy()
        show_dashboard() 

def create_profile_window():
    window = tk.Toplevel(root)
    window.title("Create Profile")

    labels = ['First Name:', 'Last Name:', 'Username:', 'Password:', 'Email:', 'Phone Number:', 'Address:', 'Bio:']
    for i, text in enumerate(labels):
        tk.Label(window, text=text).grid(row=i, column=0)
    
    entries = [tk.Entry(window) for _ in labels]
    for i, entry in enumerate(entries):
        entry.grid(row=i, column=1)
    
    tk.Button(window, text="Create", command=lambda: save_profile(entries)).grid(row=len(labels), column=0, columnspan=2)

def open_show_dashboard():
    create_dashboard_window = tk.Toplevel()
    create_dashboard = show_dashboard(create_dashboard_window)

def open_view_questions(master):
    view_question_window = tk.Toplevel(master)  
    view_screen = ViewQuestionScreen(view_question_window)

def open_quiz_screen(master):
    quiz_window = tk.Toplevel(master)
    quiz_screen = QuizScreen(quiz_window)

def open_view_results():
    messagebox.showinfo("View Results", "Open View Results window here.")

def save_profile(entries):
    data = [e.get() for e in entries]
    conn = sqlite3.connect('quiz_application.db')
    c = conn.cursor()
    c.execute("""INSERT INTO users (first_name, last_name, username, password, email, phone_number, address, bio) 
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", data)
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Profile created successfully!")
    for entry in entries:
        entry.delete(0, tk.END) 

root = tk.Tk()
root.title("Quiz Application Login")

tk.Label(root, text="Username:").grid(row=0, column=0)
tk.Label(root, text="Password:").grid(row=1, column=0)

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

tk.Button(root, text="Log In", command=lambda: login_user(username_entry.get(), password_entry.get())).grid(row=2, column=0)
tk.Button(root, text="Create Profile", command=create_profile_window).grid(row=2, column=1)

root.mainloop()
