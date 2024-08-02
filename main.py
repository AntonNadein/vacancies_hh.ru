import json

from src.api_hh import api_vacancies

if __name__ == '__main__':
    res = api_vacancies()
    print(json.dumps(res, indent=4, ensure_ascii=False))