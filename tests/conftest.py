import pytest


@pytest.fixture
def test_list_dict_input():
    return {"items": [{"name": "test1", "area": {"name": "test3"}, "salary": "test2", "alternate_url": "test4"}]}


@pytest.fixture
def test_list_dict_output():
    return [{"city": "test3", "name": "test1", "salary": "test2", "url": "test4"}]
