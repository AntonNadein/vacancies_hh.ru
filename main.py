import datetime

from src.api_hh import api_vacancies
from src.save_to_json import save_to_json

if __name__ == '__main__':
    today_date = datetime.datetime.now().strftime("%d.%m.%Y")
    request = input('Поисковой запрос: ')
    result = api_vacancies(request, city='Санкт-Петербург')

    save_to_json(result, f'{today_date}_{request}')
