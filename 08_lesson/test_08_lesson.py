import requests

base_url = "https://ru.yougile.com/api-v2"
token = "bpbOO9GWrgXzE7uEKkx8YwAtfaleiWJBuwTjKoT8eY-D0YyiKjCgEnlTj0OfSsja"
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def test_create_project():
    """Создание проекта"""
    payload = {"title": "First Project"}
    response = requests.post(base_url + '/projects', headers=headers, json=payload)

    assert response.status_code == 201, f"Ошибка: {response.text}"
    data = response.json()
    assert "id" in data


def test_get_project():
    """Получение проекта"""
    payload = {"title": "Get_project"}
    create_resp = requests.post(base_url + '/projects', headers=headers, json=payload)
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]

    get_resp = requests.get(base_url + '/projects/' + project_id, headers=headers)
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == project_id


def test_update_project():
    """Изменение проекта"""
    payload = {"title": "Project_old"}
    create_resp = requests.post(base_url + '/projects', headers=headers, json=payload)
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]

    update_payload = {"title": "Project_new"}
    update_resp = requests.put(base_url + '/projects/' + project_id, headers=headers, json=update_payload)
    assert update_resp.status_code == 200

    get_resp = requests.get(base_url + '/projects/' + project_id, headers=headers)
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == "Project_new"


def test_create_project_without_name():
    """Негативный тест: создание проекта без названия"""
    payload = {}
    response = requests.post(base_url + '/projects', headers=headers, json=payload)
    assert response.status_code in [400, 422]


def test_get_none_exist_project():
    """Негативный тест: запрос несуществующего проекта"""
    fake_id = "госуслуги"
    response = requests.get(base_url + '/projects/' + fake_id, headers=headers)
    assert response.status_code in [400, 404]


def test_update_invalid_project():
    """Негативный тест: обновление несуществующего проекта"""
    fake_id = "госуслуги"
    payload = {"title": "invalid_update"}
    response = requests.put(base_url + '/projects/' + fake_id, headers=headers, json=payload)
    assert response.status_code in [400, 404]
