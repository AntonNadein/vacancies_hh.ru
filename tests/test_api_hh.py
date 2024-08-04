from unittest.mock import patch

from src.api_hh import api_vacancies


@patch("requests.get")
def test_api_vacancies(moc_requests, test_list_dict_input, test_list_dict_output):
    """тестирование правильной работы"""
    moc_requests.return_value.json.return_value = test_list_dict_input
    result = api_vacancies("python", exclude_text="ci", period=2, city="Moscow")
    assert result == test_list_dict_output


@patch("requests.get")
def test_api_vacancies1(moc_requests, test_list_dict_input, test_list_dict_output):
    """тестирование правильной работы с ошибкой названия города"""
    moc_requests.return_value.json.return_value = test_list_dict_input
    result = api_vacancies("python", city="Mosco")
    assert result == test_list_dict_output


@patch("requests.get")
def test_api_vacancies2(moc_requests):
    """тестирование ошибки ключа словаря"""
    moc_requests.return_value.json.return_value = {
        "ITEMS": [{"name": "test1", "area": {"name": "test3"}, "salary": "test2", "alternate_url": "test4"}]
    }
    result = api_vacancies("python", city="Mosco")
    assert result == []
