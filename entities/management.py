import datetime


class Stock:
    def __init__(self, product, category,  quantity, value, data=datetime.datetime.now().date().strftime('%m-%d-%Y')):
        self.__product = product
        self.__category = category
        self.__data = data
        self.__quantity = str(quantity)
        self.__value = str(value)

    def get_product(self):
        return self.__product

    def get_category(self):
        return self.__category

    def get_data(self):
        return self.__data

    def get_quantity(self):
        return self.__quantity

    def get_value(self):
        return self.__value

    def __str__(self) -> str:
        return f'product: {self.__product}\n' \
               f'category: {self.__category}\n' \
               f'data: {self.__data}\n' \
               f'quantity: {self.__quantity}\n' \
               f'value: {self.__value}'


class History:
    def __init__(self, product, category, quantity, value, entry_exit):
        self.__product = product
        self.__category = category
        self.__entry_exit = 'Entrada' if entry_exit else 'Saída'
        self.__data = datetime.datetime.now().date().strftime('%m-%d-%Y')
        self.__quantity = str(quantity)
        self.__value = str(value)

    def get_product(self):
        return self.__product

    def get_category(self):
        return self.__category

    def get_entry_exit(self):
        return self.__entry_exit

    def get_data(self):
        return self.__data

    def get_quantity(self):
        return self.__quantity

    def get_value(self):
        return self.__value

    def __str__(self) -> str:
        return f'product: {self.__product}\n' \
               f'category: {self.__category}\n' \
               f'entry_exit: {self.__entry_exit}\n' \
               f'data: {self.__data}\n' \
               f'quantity: {self.__quantity}\n' \
               f'value: {self.__value}'
