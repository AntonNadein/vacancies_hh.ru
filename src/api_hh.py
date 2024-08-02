import json
import logging

import requests

from src.logger import setup_logging

setup_logging()
api_vacancies_logger = logging.getLogger('app.api_vacancies')
def api_vacancies(vacancy_id=None):
    list_id = []
    url = f'https://api.hh.ru/vacancies'
    responce = requests.get(url)
    result = responce.json()['items']
    api_vacancies_logger.info('Выпонился запрос')
    for items in result:
        list_id.append(items['name'])
    api_vacancies_logger.info(f'Результат выполнения: {list_id}')

    return list_id

