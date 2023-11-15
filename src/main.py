from funcs import *

operations = sort_by_date(filter_by_state(open_file("../data/operations.json")))


for i in range(0, 5):
    print(date_info(operations[i]))
    print(operation_info(operations[i]))
    print(amount_info(operations[i]))


