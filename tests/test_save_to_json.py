import tempfile

from src.save_to_json import save_to_json


def test_log_good_file_log():
    """Тестирует запись в файл"""

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        test_file_path = tmp_file.name

    save_to_json('test_str', test_file_path)

    with open(test_file_path, "r", encoding="utf-8") as file:
        test = file.read()

    assert test == '"test_str"'
