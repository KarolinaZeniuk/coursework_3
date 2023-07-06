import json
from datetime import datetime


def get_json():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def find_last_five(content):
    """
    Возвращает список из последних пяти операций. Номер карты и счета маскирует.
    :param content:Содержимое json файла с операциями
    :return: list
    """
    # получаем список дат и сортируем в хронологическом порядке для дальнейшего поиска пяти последних операций
    dat = []
    for i in content:
        dat.append(i['date'][:10] + ' ' + i['date'][11:19])
    sorted_date = sorted(dat, reverse=True)

    # с помощью вложенного цикла проходимся по списку операций и находим пять последних, добавляем их в список
    last_five_operations = []
    counter = 0
    for a in range(len(sorted_date)):
        for i in content:
            if counter >= 5:
                break
            if i['date'][:10] + ' ' + i['date'][11:19] == sorted_date[a] and i['state'] == 'EXECUTED':
                last_five_operations.append(i)
                counter += 1
    # с помощью вложенного цикла маскируем номера карт и счетов
    for i in last_five_operations:
        for key, value in i.items():
            if 'Visa' in str(value) or 'Maestro' in str(value):
                i[key] = i[key][:-16] + i[key][-16:-12] + ' ' + i[key][-12:-10] + '' + ' ' + '****' + i[key][-4:]
            if 'Счет' in str(value):
                i[key] = i[key][:-20] + '' + i[key][-4:]

    return last_five_operations


def show_last_five(last_five_operations):
    """
    Возвращает список с информацией о последних пяти операциях в отредактированном формате.
    :param last_five_operations:
    :return: Str
    """
    result_list = []

    for i in last_five_operations:
        if 'from' in i.keys():
            result = f"{datetime.fromisoformat(i['date'][:10] + ' ' + i['date'][11:19])} {i['description']}\n" \
                     f"{i['from']} -> {i['to']}\n" \
                     f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"
            result_list.append(result)
        else:
            result = f"{datetime.fromisoformat(i['date'][:10] + ' ' + i['date'][11:19])} {i['description']}\n" \
                     f"{i['to']}\n" \
                     f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"
            result_list.append(result)

    return result_list
