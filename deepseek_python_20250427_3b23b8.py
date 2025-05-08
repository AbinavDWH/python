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
        
        # Database setup
        self.conn = sqlite3.connect('todo.db')
        self.create_tables()
        
        # Main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Calendar Frame
        self.calendar_frame = ttk.Frame(self.main_frame)
        self.calendar_frame.pack(fill=tk.BOTH, expand=True)
        
        # Analysis Button
        self.analysis_btn = ttk.Button(self.main_frame, text="Show Analysis", command=self.show_analysis)
        self.analysis_btn.pack(pady=5)
        
        self.create_calendar()
        
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            description TEXT,
                            date DATE,
                            status TEXT)''')
        self.conn.commit()
        
    def create_calendar(self):
        # Clear existing calendar
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
            
        # Calendar header
        header = ttk.Label(self.calendar_frame, text=self.current_date.strftime("%B %Y"), font=('Arial', 12, 'bold'))
        header.grid(row=0, column=0, columnspan=7)
        
        # Days of the week
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for i, day in enumerate(days):
            ttk.Label(self.calendar_frame, text=day).grid(row=1, column=i)
            
        # Calendar days
        month_days = calendar.monthcalendar(self.current_date.year, self.current_date.month)
        for week_num, week in enumerate(month_days):
            for day_num, day in enumerate(week):
                if day != 0:
                    date_str = f"{self.current_date.year}-{self.current_date.month:02d}-{day:02d}"
                    tasks = self.get_tasks(date_str)
                    btn = ttk.Button(self.calendar_frame, text=str(day), command=lambda d=date_str: self.show_tasks(d))
                    btn.grid(row=week_num+2, column=day_num, sticky='nsew')
                    self.color_button(btn, tasks)
                    
    def get_tasks(self, date_str):
        cursor = self.conn.cursor()
        cursor.execute("SELECT status FROM tasks WHERE date=?", (date_str,))
        return cursor.fetchall()
        
    def color_button(self, btn, tasks):
        if not tasks:
            btn.configure(style='TButton')
            return
            
        complete = sum(1 for t in tasks if t[0] == 'Complete')
        total = len(tasks)
        if complete == total:
            btn.configure(style='Complete.TButton')
        elif complete == 0:
            btn.configure(style='Incomplete.TButton')
        else:
            btn.configure(style='InProgress.TButton')
            
    def show_tasks(self, date_str):
        self.selected_date = datetime.strptime(date_str, "%Y-%m-%d")
        task_window = tk.Toplevel(self.root)
        task_window.title(f"Tasks for {date_str}")
        
        # Task list
        tree = ttk.Treeview(task_window, columns=('Status', 'Name'), show='headings')
        tree.heading('Status', text='Status')
        tree.heading('Name', text='Task Name')
        tree.pack(padx=10, pady=10)
        
        # Populate tasks
        cursor = self.conn.cursor()
        cursor.execute("SELECT name, status FROM tasks WHERE date=?", (date_str,))
        for task in cursor.fetchall():
            tree.insert('', 'end', values=(task[1], task[0]))
            
        # Controls
        control_frame = ttk.Frame(task_window)
        control_frame.pack(pady=5)
        
        ttk.Button(control_frame, text="Add Task", command=lambda: self.add_task(task_window, date_str)).grid(row=0, column=0)
        ttk.Button(control_frame, text="Mark Complete", command=lambda: self.update_status(tree, 'Complete')).grid(row=0, column=1)
        ttk.Button(control_frame, text="Mark In Progress", command=lambda: self.update_status(tree, 'In Progress')).grid(row=0, column=2)
        ttk.Button(control_frame, text="Delete Task", command=lambda: self.delete_task(tree)).grid(row=0, column=3)
        
    def add_task(self, parent, date_str):
        add_window = tk.Toplevel(parent)
        add_window.title("Add New Task")
        
        ttk.Label(add_window, text="Task Name:").grid(row=0, column=0)
        name_entry = ttk.Entry(add_window)
        name_entry.grid(row=0, column=1)
        
        ttk.Label(add_window, text="Description:").grid(row=1, column=0)
        desc_entry = ttk.Entry(add_window)
        desc_entry.grid(row=1, column=1)
        
        def save_task():
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO tasks (name, description, date, status) VALUES (?, ?, ?, ?)",
                          (name_entry.get(), desc_entry.get(), date_str, 'Incomplete'))
            self.conn.commit()
            add_window.destroy()
            parent.destroy()
            self.show_tasks(date_str)
            
        ttk.Button(add_window, text="Save", command=save_task).grid(row=2, columnspan=2)
        
    def update_status(self, tree, status):
        selected = tree.selection()
        if not selected:
            return
            
        task_name = tree.item(selected[0])['values'][1]
        cursor = self.conn.cursor()
        cursor.execute("UPDATE tasks SET status=? WHERE name=? AND date=?",
                      (status, task_name, self.selected_date.strftime("%Y-%m-%d")))
        self.conn.commit()
        tree.item(selected[0], values=(status, task_name))
        
    def delete_task(self, tree):
        selected = tree.selection()
        if not selected:
            return
            
        task_name = tree.item(selected[0])['values'][1]
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE name=? AND date=?",
                      (task_name, self.selected_date.strftime("%Y-%m-%d")))
        self.conn.commit()
        tree.delete(selected[0])
        
    def show_analysis(self):
        analysis_window = tk.Toplevel(self.root)
        analysis_window.title("Consistency Analysis")
        
        # Date range selection
        ttk.Label(analysis_window, text="Start Date:").grid(row=0, column=0)
        start_entry = ttk.Entry(analysis_window)
        start_entry.grid(row=0, column=1)
        
        ttk.Label(analysis_window, text="End Date:").grid(row=1, column=0)
        end_entry = ttk.Entry(analysis_window)
        end_entry.grid(row=1, column=1)
        
        def generate_report():
            try:
                start_date = datetime.strptime(start_entry.get(), "%Y-%m-%d")
                end_date = datetime.strptime(end_entry.get(), "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD")
                return
                
            cursor = self.conn.cursor()
            cursor.execute('''SELECT date, 
                            SUM(CASE WHEN status='Complete' THEN 1 ELSE 0 END) as complete,
                            COUNT(*) as total
                            FROM tasks
                            WHERE date BETWEEN ? AND ?
                            GROUP BY date''', (start_date.strftime("%Y-%m-%d"), 
                                             end_date.strftime("%Y-%m-%d")))
            
            data = cursor.fetchall()
            dates = []
            completion_rates = []
            
            for record in data:
                dates.append(record[0])
                completion_rates.append((record[1]/record[2])*100)
                
            # Streak calculation
            current_streak = 0
            max_streak = 0
            for rate in completion_rates:
                if rate == 100:
                    current_streak += 1
                    max_streak = max(max_streak, current_streak)
                else:
                    current_streak = 0
                    
            # Plotting
            fig = plt.figure(figsize=(8,4))
            ax = fig.add_subplot(111)
            ax.plot(dates, completion_rates, marker='o')
            ax.set_title("Task Completion Rate Over Time")
            ax.set_ylabel("Completion Rate (%)")
            ax.grid(True)
            
            canvas = FigureCanvasTkAgg(fig, master=analysis_window)
            canvas.draw()
            canvas.get_tk_widget().grid(row=3, columnspan=2)
            
            # Streak display
            ttk.Label(analysis_window, text=f"Longest Completion Streak: {max_streak} days").grid(row=4, columnspan=2)
            
        ttk.Button(analysis_window, text="Generate Report", command=generate_report).grid(row=2, columnspan=2)

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.configure('Complete.TButton', background='lightgreen')
    style.configure('Incomplete.TButton', background='salmon')
    style.configure('InProgress.TButton', background='lightyellow')
    app = TodoApp(root)
    root.mainloop()