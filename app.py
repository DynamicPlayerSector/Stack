import modules.functions
import os
import sys
from flask import Flask, render_template, request, redirect, url_for

current_file = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file)
os.chdir(current_directory)

PORT = 9001
DEBUG_MODE = False

base_dir = '.'
if hasattr(sys, '_MEIPASS'):
    base_dir = os.path.join(sys._MEIPASS)

app = Flask(__name__,
            static_folder=os.path.join(base_dir, 'static'),
            template_folder=os.path.join(base_dir, 'templates'))

# app.config['SERVER_NAME'] = f'localhost:{PORT}' # replace with your hostname and port number
app.config['APPLICATION_ROOT'] = '/' # replace with your root URL
app.config['PREFERRED_URL_SCHEME'] = 'https' # replace with your preferred URL scheme
app.app_context().push()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        if 'action' in request.form and request.form['action'] == 'Add task':
            user_input = request.form['input']
            modules.functions.AddTask(user_input)
            return redirect(url_for('index'))

    tasks = modules.functions.GetTasks()
    rows = ["id", "name", "check", "created_at", "archive"]
    tasks_dictionary = [dict(zip(rows, item)) for item in tasks]
    #print(tasks_dictionary)
    return render_template('/index.html', tasks = tasks, tasks_dictionary = tasks_dictionary)

@app.route('/tick', methods=['GET', 'POST'])
def index_tick():
    data = request.get_json()
    state = 1 if data['activated'] else 0
    modules.functions.TickTask(data['id'], state)

    return "Success"

@app.route('/archive', methods=['GET', 'POST'])
def index_archive():
    data = request.get_json()
    modules.functions.Archive(data['id'])

    return "Success"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = DEBUG_MODE, port = 9901)












                