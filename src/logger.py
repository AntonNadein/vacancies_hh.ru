import logging


def setup_logging():
    '''Базовая настройка логгера для всего проекта'''
    (
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            filename="logs\\hh_test.log",  # Запись логов в файл
            filemode="w",  # Перезапись файла при каждом запуске
        )
    )
    return logging.getLogger()
