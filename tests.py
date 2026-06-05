import pytest
import requests

# CRUD
BASE_URL = "http://127.0.0.1:5000"
tasks = []

def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "mensagem" in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json["id"]

def test_update_task():
    if tasks:
        tasks_id = tasks[0]
        playload = {
            "completed": True,
            "description": "Nova descrição",
            "title": "Titulo atualizado"
        }
        response = requests.put(f"{BASE_URL}/tasks/{tasks_id}", json=playload)
        response.status_code == 200
        response_json = response.json()
        assert "mensagem" in response_json

        # Nova requisição a tarefa especifica
        response = requests.get(f"{BASE_URL}/tasks/{tasks_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["title"] == playload["title"]
        assert response_json["description"] == playload["description"]
        assert response_json["completed"] == playload["completed"]

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        response.status_code == 200

        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404