from flask import Flask, render_template, request, redirect, url_for
import datetime



app = Flask(__name__)
tasks = []


@app.route('/')
def index():
    current_year = datetime.datetime.now().year
    return render_template('index.html', tasks=tasks, current_year=current_year)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
        return redirect(url_for('index'))
    else:
        return "Bad Request: Invalid data", 400

@app.route('/remove_task/<int:task_id>')
def remove_task(task_id):
    if task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
