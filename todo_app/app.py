from flask import Flask, redirect, render_template, request
from todo_app.data.trello_items import Item, add_item, get_items, update_item, remove_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template('index.html', items=sorted(get_items(), key=lambda x: x.status, reverse=True))

@app.route('/add_item', methods=["POST"])
def add_list_item():
    add_item(request.form.get('item'))
    return redirect('/')

@app.route('/update_task', methods=["POST"])
def update_task():
    task_id = request.form.get("id")
    title = request.form.get("title")
    status = request.form.get("status")
    update_item(Item(task_id, title, status))
    return redirect('/')

@app.route('/remove_task', methods=["POST"])
def remove_task():
    task_id = request.values.get("id")
    remove_item(task_id)
    return redirect('/')