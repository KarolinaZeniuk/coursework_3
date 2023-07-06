import json
from function import show_last_five, find_last_five


def test_show_last_five():
    with open('tests/test_functions/show_last_five/result.json') as file:
        result = json.load(file)

    with open('operations.json', encoding='utf8') as file:
        operations = json.load(file)

    last_five_list = find_last_five(operations)

    assert show_last_five(last_five_list) == result


test_show_last_five()
