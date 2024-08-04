import datetime

from src.api_hh import api_vacancies
from src.save_to_json import save_to_json

if __name__ == '__main__':
    today_date = datetime.datetime.now().strftime("%d.%m.%Y")
    request = input('Поисковой запрос: ')
    exclude_text = input('Введите исключение из запроса (опционально можно не вводить): ')
    city_request = input('Введите город с большой буквы (опционально можно не вводить): ')
    result = api_vacancies(request, exclude_text=exclude_text, city=city_request)

    save_to_json(result, f'{today_date}_{request}')
