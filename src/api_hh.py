import logging

import requests

from src.logger import setup_logging

setup_logging()
api_vacancies_logger = logging.getLogger("app.api_vacancies")
# Словарь Город: id на hh.ru может быть дополнен
city_dict = {"Москва": 1, "Санкт-Петербург": 2, "Екатеринбург": 3, "Новосибирск": 4}


def api_vacancies(search_text: str, exclude_text: str = None, city: str = None, period: int = 1) -> list[dict]:
    """
    Функция запроса и преобразования данных с hh.ru.
    :param search_text: str Текст поиска.
    :param exclude_text: str Текст исключения из поиска.
    :param city: str Названия города с большой буквы.
    :param period: int Количество дней для поиска.
    :return: список словарей [вакансия, зарплата, город, url].
    """
    list_item = []

    if city in city_dict:
        city_key = city_dict[city]
    else:
        city_key = None
    api_vacancies_logger.info(f"Проверка названия города, если не задано или не пройдено то <None>: {city_key}")

    try:
        # данные для запроса
        url = "https://api.hh.ru/vacancies"
        params = {
            "text": search_text,
            "exclude": exclude_text,
            "search_field": "name",
            "area": city_key,
            "period": period,
            "only_with_salary": True,
        }
        # тело запроса
        responce = requests.get(url, params)
        api_vacancies_logger.info(f"Выпонился {responce}")
        vacancies_data = responce.json()["items"]
        api_vacancies_logger.info("Выпонился запрос")
        # формирование отчета
        for vacancies in vacancies_data:
            vacancies_dict = {
                "name": vacancies["name"],
                "salary": vacancies["salary"],
                "city": vacancies["area"]["name"],
                "url": vacancies["alternate_url"],
            }
            list_item.append(vacancies_dict)

        return list_item
    except Exception as ex:
        api_vacancies_logger.error(f"Произошла ошибка: {ex}")
        return []
