import pytest
import requests

#CRUD
BASE_URL = 'http://127.0.0.1:5000'
tasks =[]

def test_create_task():
  new_task_data = {
    "title": "Nova tarefa",
    "description": "Descrição da nova tarefa"
  }

  response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
  #assert response.status.code == 200
  assert "data" in response.json()
  assert "id" in response.json()
  tasks.append(response.json()['id'])