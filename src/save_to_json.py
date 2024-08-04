import json
import logging
import os

from src.logger import setup_logging

setup_logging()
save_to_json_logger = logging.getLogger("app.save_to_json")


def save_to_json(list_dict_for_json: list[dict], file_name: str = "vacancies") -> None:
    """
    Функция сохранения словаря в файл json
    :param list_dict_for_json: Список словарей.
    :param file_name: Имя файла в который бует совершено сохранение.
    """
    PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "..", "data", file_name)
    save_to_json_logger.info(f"Путь до файла: {PATH_TO_FILE}")
    try:
        with open(PATH_TO_FILE, "w", encoding="utf-8") as file:
            json.dump(list_dict_for_json, file, ensure_ascii=False, indent=4)
        save_to_json_logger.info("Файл сохранен")
    except Exception as ex:
        save_to_json_logger.error(f"Произошла ошибка: {ex}")
