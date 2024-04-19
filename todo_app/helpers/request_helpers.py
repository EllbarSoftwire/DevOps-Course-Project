from todo_app.data.trello_items import Item


def get_item_from_request(request):
  task_id = request.form.get("id")
  title = request.form.get("title")
  status = request.form.get("status")
  return Item(task_id, title, status)
