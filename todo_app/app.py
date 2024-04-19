from flask import Flask, redirect, render_template, request
from todo_app.data.trello_items import Item, add_item, get_items, set_complete, set_in_progress, set_not_started, remove_item

from todo_app.flask_config import Config
from todo_app.helpers.request_helpers import get_item_from_request
from todo_app.view_model import ViewModel

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())


    @app.route('/')
    def index():
        item_view_model = ViewModel(get_items())
        return render_template('index.html', view_model=item_view_model)

    @app.route('/add_item', methods=["POST"])
    def add_list_item():
        add_item(request.form.get('item'))
        return redirect('/')

    @app.route('/set_complete', methods=["POST"])
    def complete_task():
        item = get_item_from_request(request)
        set_complete(item)
        return redirect('/')

    @app.route('/set_in_progress', methods=["POST"])
    def in_progress_task():
        item = get_item_from_request(request)
        set_in_progress(item)
        return redirect('/')

    @app.route('/set_not_started', methods=["POST"])
    def not_started_task():
        item = get_item_from_request(request)
        set_not_started(item)
        return redirect('/')

    @app.route('/remove_task', methods=["POST"])
    def remove_task():
        task_id = request.values.get("id")
        remove_item(task_id)
        return redirect('/')
    
    return app