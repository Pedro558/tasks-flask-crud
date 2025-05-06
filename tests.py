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
  assert response.status_code == 200
  assert "data" in response.json()
  assert "id" in response.json()
  tasks.append(response.json()['id'])

def test_get_tasks():
  response = requests.get(f"{BASE_URL}/tasks")
  assert response.status_code == 200
  assert "tasks" in response.json()
  assert "total_tasks" in response.json()

def test_get_task():
  if tasks:
    task_id = tasks[0]
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    assert task_id == response.json()['id']
