import tkinter as tk
from tkinter import messagebox
import sqlite3
from create_quiz import CreateQuiz

def login_user(username, password):
    conn = sqlite3.connect('quiz_application.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    account = c.fetchone()
    conn.close()
    
    if account:
        messagebox.showinfo("Login Success", "You have successfully logged in!")
        root.destroy()  # Close the login window
        show_dashboard()  # Open the dashboard


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

def show_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Dashboard")
    
    tk.Label(dashboard, text="Welcome to the Dashboard!", font=('Helvetica', 16)).pack(pady=20)
    
    tk.Button(dashboard, text="Create Quiz", command=open_create_quiz).pack(side=tk.TOP, anchor=tk.W, padx=5, pady=1)
    tk.Button(dashboard, text="View Quiz Results", command=open_view_results).pack(side=tk.TOP, anchor=tk.W, padx=5, pady=1)
    dashboard.mainloop()

def open_create_quiz():
    # This standalone function correctly opens the Create Quiz window
    create_quiz_window = tk.Toplevel()  # Create a new top-level window
    create_quiz_app = CreateQuiz(create_quiz_window)

def open_view_results():
    messagebox.showinfo("View Results", "Open View Results window here.")


def save_profile(entries):
    # Extract data from entries and save to the database
    data = [e.get() for e in entries]
    conn = sqlite3.connect('quiz_application.db')
    c = conn.cursor()
    c.execute("""INSERT INTO users (first_name, last_name, username, password, email, phone_number, address, bio) 
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", data)
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Profile created successfully!")
    for entry in entries:
        entry.delete(0, tk.END)  # Clear form after submission

# Main login window
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
