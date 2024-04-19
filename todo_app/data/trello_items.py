import json
import os
import requests
 

def get_api_url():
  return "https://api.trello.com/1"

class Item:
  def __init__(self, id, name, status = "Not Started"):
    self.id = id
    self.name = name
    self.status = status
  
  def from_trello_card(cls, card):
    return cls(card['id'], card['name'],  _get_status_from_list_id(card["idList"]))

def get_base_query():
  return {
  "key": os.getenv("TRELLO_API_KEY"),
  "token": os.getenv("TRELLO_API_TOKEN")
}

def get_headers():
  return {
  "Accept": "application/json"
}

def add_item(title):
  url = f"{get_api_url()}/cards"

  query = get_base_query() | {
    "idList": os.getenv("TRELLO_BOARD_ID"),
    "name": title,
  } 

  requests.request(
    "POST",
    url,
    headers=get_headers(),
    params=query
  )

def _get_status_from_list_id(list):
  if list == os.getenv("TRELLO_FINISHED_LIST_ID"):
    return "Completed"
  if list == os.getenv("TRELLO_IN_PROGRESS_LIST"):
    return "In Progress"
  if list == os.getenv("TRELLO_NOT_STARTED_LIST_ID"):
    return "Not Started"
  return "Other"

def get_items():
  id = os.getenv("TRELLO_BOARD_ID")
  url = f"{get_api_url()}/boards/{id}/cards"
  response = requests.get(
    url,
    headers=get_headers(),
    params=get_base_query()
  )
  items = []
  body = response.json()
  for card in body:
    items.append(Item(
      card["id"],
      card["name"], 
      _get_status_from_list_id(card["idList"])))
  return items

def set_complete(item):
  _update_item(item, os.getenv("TRELLO_FINISHED_LIST_ID"))

def set_in_progress(item):
  _update_item(item, os.getenv("TRELLO_IN_PROGRESS_LIST"))

def set_not_started(item):
  _update_item(item, os.getenv("TRELLO_NOT_STARTED_LIST_ID"))

def _update_item(item, idList):
  url = f"{get_api_url()}/cards/{item.id}"
  query = get_base_query() | {
    "name": item.name,
    "idList": idList
  }
  requests.request(
    "PUT",
    url,
    headers=get_headers(),
    params=query
  )

def remove_item(id):
  url = f"{get_api_url()}/cards/{id}"
  requests.request(
    "DELETE",
    url,
    headers=get_headers(),
    params=get_base_query()
  )