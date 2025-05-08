import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import calendar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Yearly Task Manager")
        self.current_date = datetime.now()
        self.selected_date = self.current_date
        
        # Database setup with error handling
        try:
            self.conn = sqlite3.connect('todo.db')
            self.create_tables()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to initialize database:\n{str(e)}")
            self.root.destroy()
            return
            
        # Rest of initialization
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.create_styles()
        self.create_widgets()
        
    def create_styles(self):
        self.style = ttk.Style()
        self.style.configure('Complete.TButton', background='lightgreen')
        self.style.configure('Incomplete.TButton', background='salmon')
        self.style.configure('InProgress.TButton', background='lightyellow')

    def create_widgets(self):
        # Calendar Frame
        self.calendar_frame = ttk.Frame(self.main_frame)
        self.calendar_frame.pack(fill=tk.BOTH, expand=True)
        
        # Analysis Button
        self.analysis_btn = ttk.Button(self.main_frame, text="Show Analysis", command=self.show_analysis)
        self.analysis_btn.pack(pady=5)
        
        self.create_calendar()

    def create_tables(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                description TEXT,
                                date DATE NOT NULL,
                                status TEXT NOT NULL)''')
            self.conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to create tables:\n{str(e)}")
            raise

    # ... (rest of the methods remain the same but add error handling to database operations)

    def get_tasks(self, date_str):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT status FROM tasks WHERE date=?", (date_str,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to fetch tasks:\n{str(e)}")
            return []

    def show_tasks(self, date_str):
        try:
            self.selected_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Date Error", "Invalid date format")
            return

        # ... (rest of show_tasks method with error handling)

if __name__ == "__main__":
    root = tk.Tk()
    try:
        app = TodoApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Critical Error", f"Application failed to start:\n{str(e)}")