import json
import os
import requests

KEY = os.getenv("TRELLO_API_KEY")
TOKEN = os.getenv("TRELLO_API_TOKEN")
BOARD_ID = os.getenv("TRELLO_BOARD_ID")
NOT_STARTED_COLUMN = os.getenv("TRELLO_NOT_STARTED_LIST_ID")
FINISHED_COLUMN = os.getenv("TRELLO_FINISHED_LIST_ID")
TRELLO_API = "https://api.trello.com/1"

class Item:
  def __init__(self, id, name, status = "Not Started"):
    self.id = id
    self.name = name
    self.status = status
  
  def from_trello_card(cls, card):
    return cls(card['id'], card['name'],  ("Completed" if card["idList"] == FINISHED_COLUMN else "Not Started"))

BASE_QUERY = {
  "key": KEY,
  "token": TOKEN
}

HEADERS = {
  "Accept": "application/json"
}

def add_item(title):
  url = f"{TRELLO_API}/cards"

  query = BASE_QUERY | {
    "idList": "65cf68e717e5358c95f22842",
    "name": title,
  } 

  requests.request(
    "POST",
    url,
    headers=HEADERS,
    params=query
  )

def get_items():
  url = f"{TRELLO_API}/boards/{BOARD_ID}/cards"
  response = requests.request(
    "GET",
    url,
    headers=HEADERS,
    params=BASE_QUERY
  )
  items = []
  body = json.loads(response.text)
  for card in body:
    items.append(Item(card["id"], card["name"], "Completed" if card["idList"] == FINISHED_COLUMN else "Not Started"))
  return items

def update_item(item):
  url = f"{TRELLO_API}/cards/{item.id}"
  idList = FINISHED_COLUMN if item.status == "Completed" else NOT_STARTED_COLUMN
  query = BASE_QUERY | {
    "name": item.name,
    "idList": idList
  }
  requests.request(
    "PUT",
    url,
    headers=HEADERS,
    params=query
  )

def remove_item(id):
  url = f"{TRELLO_API}/cards/{id}"
  requests.request(
    "DELETE",
    url,
    headers=HEADERS,
    params=BASE_QUERY
  )