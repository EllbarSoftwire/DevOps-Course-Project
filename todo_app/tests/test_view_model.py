from todo_app.data.trello_items import Item
from todo_app.view_model import ViewModel


def test_view_model_done_items():
  # Given
  items = [Item("1", "Item 1", "Completed")]
  model = ViewModel(items=items)

  # When
  actual = model.done_items

  # Then
  assert actual == items

def test_view_model_done_items_only_returns_done_items():
  # Given
  items = [Item("1", "Item 1", "Completed"), Item("2", "Item 2", "Not Started"), Item("3", "Item 3", "In Progress")]
  model = ViewModel(items=items)

  # When
  actual = model.done_items

  # Then 
  assert actual == [items[0]]

def test_view_model_not_started_items():
  # Given
  items = [Item("1", "Item 1", "Not Started")]
  model = ViewModel(items=items)

  # When
  actual = model.not_done_items

  # Then
  assert actual == items

def test_view_model_not_started_items_only_returns_not_started_items():
  # Given
  items = [Item("1", "Item 1", "Completed"), Item("2", "Item 2", "Not Started"), Item("3", "Item 3", "In Progress")]
  model = ViewModel(items=items)

  # When
  actual = model.not_done_items

  # Then 
  assert actual == [items[1]]

def test_view_model_inm_progress_items():
  # Given
  items = [Item("1", "Item 1", "In Progress")]
  model = ViewModel(items=items)

  # When
  actual = model.in_progress_items

  # Then
  assert actual == items

def test_view_model_in_progress_items_only_returns_in_progress_items():
  # Given
  items = [Item("1", "Item 1", "Completed"), Item("2", "Item 2", "Not Started"), Item("2", "Item 2", "In Progress")]
  model = ViewModel(items=items)

  # When
  actual = model.in_progress_items

  # Then 
  assert actual == [items[2]]
