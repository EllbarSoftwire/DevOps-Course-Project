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
    return cls(card['id'], card['name'],  ("Completed" if card["idList"] == os.getenv("TRELLO_FINISHED_LIST_ID") else "Not Started"))

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

def get_items():
  url = f"{get_api_url()}/boards/{os.getenv("TRELLO_BOARD_ID")}/cards"
  response = requests.request(
    "GET",
    url,
    headers=get_headers(),
    params=get_base_query()
  )
  items = []
  body = json.loads(response.text)
  for card in body:
    items.append(Item(card["id"], card["name"], "Completed" if card["idList"] == os.getenv("TRELLO_FINISHED_LIST_ID") else "Not Started"))
  return items

def update_item(item):
  url = f"{get_api_url()}/cards/{item.id}"
  idList = os.getenv("TRELLO_FINISHED_LIST_ID") if item.status == "Completed" else os.getenv("TRELLO_NOT_STARTED_LIST_ID")
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