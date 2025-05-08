import React, { useState, useEffect } from 'react';
import { Calendar } from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import { openDB } from 'idb';

// IndexedDB setup
const DB_NAME = 'yearly-todo-db';
const DB_VERSION = 1;
const STORE_NAME = 'tasks';

async function initDB() {
  return openDB(DB_NAME, DB_VERSION, {
    upgrade(db) {
      if (!db.objectStoreNames.contains(STORE_NAME)) {
        db.createObjectStore(STORE_NAME, { keyPath: 'id' });
      }
    },
  });
}

async function getAllTasks(db) {
  return (await db).getAll(STORE_NAME);
}

async function addTaskToDB(db, task) {
  return (await db).put(STORE_NAME, task);
}

async function updateTaskInDB(db, task) {
  return (await db).put(STORE_NAME, task);
}

export default function TodoApp() {
  const [tasks, setTasks] = useState([]);
  const [selectedDate, setSelectedDate] = useState(new Date());
  const [db, setDb] = useState(null);

  // Init DB and load tasks
  useEffect(() => {
    (async () => {
      const database = await initDB();
      setDb(database);
      const all = await getAllTasks(database);
      setTasks(all || []);
    })();
  }, []);

  // Add new task
  async function addTask(title) {
    const newTask = { id: Date.now(), title, status: 'incomplete', date: selectedDate.toISOString() };
    setTasks(prev => [...prev, newTask]);
    await addTaskToDB(db, newTask);
  }

  // Update status
  async function updateStatus(id, status) {
    setTasks(prev => {
      const updated = prev.map(t => t.id === id ? { ...t, status } : t);
      updated.forEach(t => {
        if (t.id === id) updateTaskInDB(db, t);
      });
      return updated;
    });
  }

  const tasksForDay = tasks.filter(
    t => new Date(t.date).toDateString() === selectedDate.toDateString()
  );

  // Analytics: consistency
  const daysWithTasks = [...new Set(tasks.map(t => new Date(t.date).toDateString()))];
  const consistency = ((daysWithTasks.length / 365) * 100).toFixed(1);

  return (
    <div className="p-4 max-w-4xl mx-auto">
      <h1 className="text-xl font-bold mb-4">Yearly To-Do Tracker</h1>
      <div className="flex gap-4">
        <div>
          <Calendar onChange={setSelectedDate} value={selectedDate} />
        </div>
        <div className="flex-1">
          <DayTasks date={selectedDate} tasks={tasksForDay} addTask={addTask} updateStatus={updateStatus} />
          <Analytics consistency={consistency} totalTasks={tasks.length} />
        </div>
      </div>
    </div>
  );
}

function DayTasks({ date, tasks, addTask, updateStatus }) {
  const [newTitle, setNewTitle] = useState('');
  return (
    <div>
      <h2 className="font-semibold">Tasks for {date.toDateString()}</h2>
      <ul className="mb-2">
        {tasks.map(t => (
          <li key={t.id} className="flex items-center gap-2">
            <span>{t.title}</span>
            <select value={t.status} onChange={e => updateStatus(t.id, e.target.value)}>
              <option value="incomplete">Incomplete</option>
              <option value="in-progress">In Progress</option>
              <option value="complete">Complete</option>
            </select>
          </li>
        ))}
      </ul>
      <div className="flex gap-2">
        <input
          className="border p-1 flex-1"
          placeholder="New task"
          value={newTitle}
          onChange={e => setNewTitle(e.target.value)}
        />
        <button
          className="px-4 py-1 bg-blue-500 text-white rounded"
          onClick={() => {
            if (newTitle.trim()) {
              addTask(newTitle.trim());
              setNewTitle('');
            }
          }}
        >Add</button>
      </div>
    </div>
  );
}

function Analytics({ consistency, totalTasks }) {
  return (
    <div className="mt-4 border-t pt-2">
      <h3 className="font-semibold">Analytics</h3>
      <p>Tasks created: {totalTasks}</p>
      <p>Consistency: {consistency}% days logged</p>
    </div>
  );
}
