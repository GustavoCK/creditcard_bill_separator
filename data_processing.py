from pdf_reader import list_of_lists


def safe_input():
    x = input()
    if x not in ['0', '1', '2', '3']:
        print("Error! 1, 2 and 3 are the only three valid inputs or 0 to discard a bill")
        x = safe_input()
    if x == '0':
        return None
    else:
        return int(x) - 1


class Bill:
    def __init__(self, store_name, purchase_value, buyer, purchase_date):
        self.store = store_name
        self.bill = purchase_value
        self.buyer = buyer
        self.date = purchase_date


class_list = []
buyers = ('Mary', 'Joel', 'Carlos')

for i in list_of_lists:
    print(i)

    number = safe_input()
    if number is None:
        pass
    else:
        class_list.append(Bill(i[1], i[2], buyers[number], i[0]))
