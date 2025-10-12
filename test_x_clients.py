import requests

base_url = "http://5.101.50.27:8000"


def test_get_active_companies():
    # Получить список всех компаний
    resp = requests.get(base_url+'/company/list')
    full_list = resp.json()

    # Получить список активных компаний
    resp = requests.get(base_url+'/company/list?active=true')
    filtered_list = resp.json()

    # Проверить, что список 1 > списка 2
    assert len(full_list) > len(filtered_list)
