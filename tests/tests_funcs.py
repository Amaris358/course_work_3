from src import funcs


def test_card_number_private():
    assert funcs.card_number_private("1234567890123456") == "1234 56** **** 3456"
    assert funcs.card_number_private("Visa 1111555599996666") == "1111 55** **** 6666"


def test_account_number_private():
    assert funcs.account_number_private("123448567890123456") == "**3456"
    assert funcs.account_number_private("Счет 2111555599996666") == "**6666"


def test_sort_by_date():
    assert funcs.sort_by_date(funcs.open_file("test_2.json")) == [{'date': '2022-12-26T10:50:58.294041'}, {'date': '2022-08-26T10:50:58.294041'}, {'date': '2021-08-26T10:50:58.294041'}, {'date': '2020-08-26T10:50:58.294041'}, {'date': '2019-08-26T10:50:58.294041'}, {'date': '2019-03-23T01:09:46.296404'}, {'date': '2018-08-19T04:27:37.904916'}, {'date': '2018-06-30T02:08:58.425572'}, {'date': '2018-03-23T10:45:06.972075'}, {'date': '2017-08-26T10:50:58.294041'}]


def test_open_file():
    assert funcs.open_file("test_2.json") == [{'date': '2019-08-26T10:50:58.294041'}, {'date': '2018-06-30T02:08:58.425572'}, {'date': '2018-03-23T10:45:06.972075'}, {'date': '2019-03-23T01:09:46.296404'}, {'date': '2018-08-19T04:27:37.904916'}, {'date': '2017-08-26T10:50:58.294041'}, {'date': '2020-08-26T10:50:58.294041'}, {'date': '2021-08-26T10:50:58.294041'}, {'date': '2022-08-26T10:50:58.294041'}, {'date': '2022-12-26T10:50:58.294041'}]


def test_date_info():
    assert funcs.date_info(funcs.open_file("operations.json")[0]) == "26.08.2019 Перевод организации"
    assert funcs.date_info(funcs.open_file("operations.json")[3]) == "23.03.2018 Открытие вклада"
    assert funcs.date_info(funcs.open_file("operations.json")[4]) == "04.04.2019 Перевод со счета на счет"


def test_operation_info():
    assert funcs.operation_info(funcs.open_file("operations.json")[0]) == "Maestro 1596 83** **** 5199 -> Cчет **9589"
    assert funcs.operation_info(funcs.open_file("operations.json")[3]) == "Cчет **2431"
    assert funcs.operation_info(funcs.open_file("operations.json")[4]) == "Cчет **8542 -> Cчет **4188"


def test_amount_info():
    assert funcs.amount_info(funcs.open_file("operations.json")[0]) == "31957.58 руб.\n"
    assert funcs.amount_info(funcs.open_file("operations.json")[1]) == "8221.37 USD\n"
    assert funcs.amount_info(funcs.open_file("operations.json")[2]) == "9824.07 USD\n"


