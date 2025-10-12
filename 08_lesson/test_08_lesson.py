import pytest
import requests

base_url = "https://ru.yougile.com/api-v2"
token = "ТОКЕН"
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def test_create_project():
    """Проверка создания проекта"""
    payload = {"name": "pytest_project"}
    response = requests.post(base_url + '/projects', headers=headers, json=payload)

    assert response.status_code == 200, f"Ошибка: {response.text}"
    data = response.json()
    assert "id" in data and data["name"] == "pytest_project"

    # Очистка данных
    # project_id = data["id"]
    # requests.delete(base_url + '/projects/' + project_id, headers=headers)


def test_get_project():
    """Проверка получения проекта"""
    # Сначала создаём проект
    payload = {"name": "pytest_get"}
    create_resp = requests.post(base_url + '/projects', headers=headers, json=payload)
    assert create_resp.status_code == 200
    project_id = create_resp.json()["id"]

    # Проверяем, что проект можно получить
    get_resp = requests.get(base_url + '/projects/' + project_id, headers=headers)
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == project_id

    # Удаляем после теста
    # requests.delete(f"{base_url}/projects/{project_id}", headers=headers)


def test_update_project():
    """Проверка обновления проекта"""
    # Создаём проект
    payload = {"name": "pytest_old"}
    create_resp = requests.post(base_url + '/projects', headers=headers, json=payload)
    assert create_resp.status_code == 200
    project_id = create_resp.json()["id"]

    # Обновляем его
    update_payload = {"name": "pytest_new"}
    update_resp = requests.put(base_url + '/projects/' + project_id, headers=headers, json=update_payload)
    assert update_resp.status_code == 200
    assert update_resp.json()["name"] == "pytest_new"

    # Удаляем после теста
    # requests.delete(f"{base_url}/projects/{project_id}", headers=headers)


def test_create_project_without_name():
    """Негативный тест — создание проекта без имени"""
    payload = {}
    response = requests.post(base_url + '/projects', headers=headers, json=payload)
    assert response.status_code in [400, 422]


def test_get_none_exist_project():
    """Негативный тест — запрос несуществующего проекта"""
    fake_id = "госуслуги"
    response = requests.get(base_url + '/projects/' + fake_id, headers=headers)
    assert response.status_code in [400, 404]


def test_update_invalid_project():
    """Негативный тест — обновление несуществующего проекта"""
    fake_id = "госуслуги"
    payload = {"name": "invalid_update"}
    response = requests.put(base_url + '/projects/' + fake_id, headers=headers, json=payload)
    assert response.status_code in [400, 404]
