import json
import io
from datetime import datetime as dt
from typing import List, Dict, Optional


def open_file(filename):
    """
    Открывает указнный файл и считывает его
    :param filename: Имя файла, который нужно открыть и считать
    :return: Данные из файла
    """
    with io.open(filename, encoding='utf-8') as file_for_read:
        all_data = file_for_read.read()
        return_data = json.loads(all_data)
        return return_data


def filter_by_state(data: List[Dict[str, str]], state: Optional[str] = "EXECUTED") -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по передаваемому значению
    :param data: список словарей
    :param state: параметр для фильтрации
    :return: Отфильтрованные данные
    """
    filter_data = list(filter(lambda x: x.get("state") == state, data))
    return filter_data


def sort_by_date(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Сортирует спписок словарей по дате по убыванию
    :param data: Списорк словарей
    :return: Отсортированный список словарей
    """
    date_list = list(filter(lambda x: x.get("date"), data))

    date_list = sorted(
        date_list,
        key=lambda x: dt.strptime(x['date'].split(".")[0], '%Y-%m-%dT%H:%M:%S'), reverse=True
    )

    return date_list


def card_number_private(card):
    """
    Из передаваемого списка берёт номер карты и маскирует его
    :param card: Номер карты
    :return: Замаскированный номер карты
    """
    card_number = card.split()[-1]

    private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]

    chunks, chunk_size = len(private_number), len(private_number) // 4
    return " ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)])


def account_number_private(account):
    """
    Маскирует номер счета
    :param card: Номер счета
    :return: Замаскированный номер счета
     """
    account_number = account.split()[-1]

    private_number = "**" + account_number[-4:]

    chunks = len(private_number)
    return "".join([private_number[i:i + 1] for i in range(0, chunks)])


def date_info(operation):
    """
    Выводит информацию о дате операции и её описание
    :param operation: Опреация, о которой необохимо получить информацию
    :return: Строку, содержащую информацию о дате операции и её описание
    """
    new_format_date = dt.strptime(operation['date'].split(".")[0], '%Y-%m-%dT%H:%M:%S')
    if "description" in operation:
        return "".join([new_format_date.strftime("%d.%m.%Y"), " ", operation["description"]])
    else:
        return new_format_date.strftime("%d.%m.%Y")


def operation_info(operation):
    """
    Выводит информацию о переводе, если она есть (откуда и куда совершён перевод)
    :param operation: Опреация, о которой необохимо получить информацию
    :return: Строку, содержащую информацию о переводе
    """
    money_transfer = []
    if "from" in operation:
        if len(operation["from"].split()[-1]) != 16:
            money_transfer.extend(["Cчет ", account_number_private(operation["from"]), ' -> '])
        else:
            split_number = operation["from"].split()[:-1]
            for k in range(0, len(split_number)):
                money_transfer.extend([split_number[k], ' '])
            money_transfer.extend([card_number_private(operation["from"]), ' -> '])
    if "to" in operation:
        if len(operation["to"].split()[-1]) != 16:
            money_transfer.extend(["Cчет ", account_number_private(operation["to"])])
        else:
            split_number = operation["to"].split()[:-1]
            for k in range(0, len(split_number)):
                money_transfer.extend([split_number[k], ' '])
            money_transfer.append(card_number_private(operation["to"]))
    return "".join(money_transfer)


def amount_info(operation):
    """
    Выводит информацию о переведенных средствах
    :param operation: Опреация, о которой необохимо получить информацию
    :return: Строку, содержащую информацию о переведенных средствах
    """
    return "".join([operation["operationAmount"]["amount"], " ", operation["operationAmount"]["currency"]["name"], "\n"])







