from flask import Flask, redirect, render_template, request
from todo_app.data.session_items import add_item, get_item, get_items, remove_item, save_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template('index.html', items=sorted(get_items(), key=lambda x: x['status'], reverse=True))

@app.route('/add_item', methods=["POST"])
def add_list_item():
    add_item(request.form.get('item'))
    return redirect('/')

@app.route('/update_task', methods=["POST"])
def update_task():
    task_id = request.form.get("id")
    title = request.form.get("title")
    status = request.form.get("status")
    save_item({'id': int(task_id), 'status': status, 'title': title,})
    return redirect('/')

@app.route('/remove_task', methods=["POST"])
def remove_task():
    task_id = request.values.get("id")
    remove_item(task_id)
    return redirect('/')