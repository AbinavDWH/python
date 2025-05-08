import sqlite3
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Database setup
conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY, title TEXT, date TEXT, 
             priority TEXT, status TEXT)''')
conn.commit()

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Year-Long To-Do Tracker")
        
        # Task Entry Frame
        entry_frame = ttk.Frame(root)
        entry_frame.pack(padx=10, pady=10)
        
        ttk.Label(entry_frame, text="Title:").grid(row=0, column=0)
        self.title_entry = ttk.Entry(entry_frame, width=30)
        self.title_entry.grid(row=0, column=1)
        
        ttk.Label(entry_frame, text="Date:").grid(row=0, column=2)
        self.date_entry = ttk.Entry(entry_frame, width=12)
        self.date_entry.grid(row=0, column=3)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        
        ttk.Label(entry_frame, text="Priority:").grid(row=0, column=4)
        self.priority = ttk.Combobox(entry_frame, values=["High", "Medium", "Low"])
        self.priority.grid(row=0, column=5)
        self.priority.set("Medium")
        
        ttk.Button(entry_frame, text="Add Task", command=self.add_task).grid(row=0, column=6)
        
        # Calendar Frame
        calendar_frame = ttk.Frame(root)
        calendar_frame.pack(padx=10, pady=10)
        
        self.cal = Calendar(calendar_frame, selectmode='day', 
                           year=datetime.now().year, 
                           month=datetime.now().month,
                           day=datetime.now().day)
        self.cal.pack(side=tk.LEFT)
        self.cal.bind("<<CalendarSelected>>", self.show_daily_tasks)
        
        self.task_list = tk.Listbox(calendar_frame, width=50, height=10)
        self.task_list.pack(side=tk.RIGHT, padx=10)
        self.task_list.bind("<Double-1>", self.toggle_status)
        
        # Analytics Frame
        analytics_frame = ttk.Frame(root)
        analytics_frame.pack(padx=10, pady=10)
        
        self.figure = plt.Figure(figsize=(6, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=analytics_frame)
        self.canvas.get_tk_widget().pack()
        
        ttk.Button(analytics_frame, text="Show Analytics", 
                  command=self.show_analytics).pack(pady=5)
        
        self.update_calendar()
        
    def add_task(self):
        title = self.title_entry.get()
        date = self.date_entry.get()
        priority = self.priority.get()
        
        if title and date:
            c.execute("INSERT INTO tasks (title, date, priority, status) VALUES (?, ?, ?, ?)",
                     (title, date, priority, "incomplete"))
            conn.commit()
            self.update_calendar()
            self.title_entry.delete(0, tk.END)
            
    def update_calendar(self):
        self.cal.calevent_remove('all')
        c.execute("SELECT date, priority FROM tasks")
        tasks = c.fetchall()
        for task in tasks:
            date = datetime.strptime(task[0], "%Y-%m-%d").date()
            self.cal.calevent_create(date, "", tags=task[1].lower())
            self.cal.tag_config(task[1].lower(), 
                              background=self.get_priority_color(task[1]))
            
    def show_daily_tasks(self, event=None):
        selected_date = self.cal.get_date()
        formatted_date = datetime.strptime(selected_date, "%m/%d/%y").strftime("%Y-%m-%d")
        
        self.task_list.delete(0, tk.END)
        c.execute("SELECT * FROM tasks WHERE date=?", (formatted_date,))
        tasks = c.fetchall()
        
        for task in tasks:
            status_mark = "✓" if task[4] == "complete" else " "
            self.task_list.insert(tk.END, f"[{status_mark}] {task[1]} ({task[3]})")
            self.task_list.itemconfig(tk.END, {'fg': self.get_priority_color(task[3])})
            
    def toggle_status(self, event):
        selection = self.task_list.curselection()
        if selection:
            task_text = self.task_list.get(selection[0])
            title = task_text.split('] ')[1].split(' (')[0]
            date = self.cal.get_date()
            formatted_date = datetime.strptime(date, "%m/%d/%y").strftime("%Y-%m-%d")
            
            c.execute("SELECT status FROM tasks WHERE title=? AND date=?", 
                     (title, formatted_date))
            status = c.fetchone()[0]
            
            new_status = "complete" if status == "incomplete" else "incomplete"
            c.execute("UPDATE tasks SET status=? WHERE title=? AND date=?",
                     (new_status, title, formatted_date))
            conn.commit()
            self.show_daily_tasks()
            
    def show_analytics(self):
        c.execute("SELECT date, COUNT(*) FROM tasks WHERE status='complete' GROUP BY date")
        data = c.fetchall()
        
        if not data:
            return
            
        dates = [datetime.strptime(d[0], "%Y-%m-%d") for d in data]
        counts = [d[1] for d in data]
        
        self.ax.clear()
        self.ax.plot(dates, counts, marker='o')
        self.ax.set_title("Task Completion Over Time")
        self.ax.set_xlabel("Date")
        self.ax.set_ylabel("Completed Tasks")
        self.canvas.draw()
        
    def get_priority_color(self, priority):
        return {"High": "red", "Medium": "orange", "Low": "green"}[priority]

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
    conn.close()