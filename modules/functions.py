import sqlite3
from datetime import datetime
from flask import current_app, url_for
from app import app
import os

with app.app_context():
    databasePath = os.path.join(current_app.root_path, 'static', 'sqlite', 'database.sqlite')

print(databasePath)

def AddTask(name):
    connection = sqlite3.connect(databasePath, check_same_thread=False)
    cursor = connection.cursor()
    now = datetime.utcnow()
    isonow = now.isoformat("T")
    order = f"INSERT INTO tasks (name, created_at) VALUES ('{name}', '{isonow}');"

    cursor.execute(order)
    connection.commit()
    connection.close()

def GetTasks():
    connection = sqlite3.connect(databasePath, check_same_thread=False)
    tasks = []
    order = "select * from tasks"


    cursor = connection.cursor()
    cursor.execute(order)
    tasks = cursor.fetchall()

    connection.close()
    return tasks

def TickTask(id, value):
    connection = sqlite3.connect(databasePath, check_same_thread=False)
    order = f"UPDATE tasks SET 'check' = {value} WHERE id = {id}"


    cursor = connection.cursor()
    cursor.execute(order)
    connection.commit()

    connection.close()
    return None

def Archive(id):
    connection = sqlite3.connect(databasePath, check_same_thread=False)
    order = f"UPDATE tasks SET 'archive' = 1 WHERE id = {id}"


    cursor = connection.cursor()
    cursor.execute(order)
    connection.commit()

    connection.close()
    return None