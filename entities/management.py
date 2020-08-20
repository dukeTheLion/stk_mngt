import pandas as pd
import datetime


class Stock:
    def __init__(self, product, category, quantity, value):
        self.__head = ['Produto', 'Categoria', 'Data de registro', 'Quantidade', 'Valor/kg']
        self.__data = [product, category, datetime.datetime.now().date().strftime('%m-%d-%Y'), quantity, value]

    def get_head(self):
        return self.__head

    def get_data(self):
        return self.__data

    def get_df(self) -> pd.DataFrame:
        return pd.DataFrame({i: j for i, j in zip(self.__head, self.__data)}, index=[0])

    def __str__(self) -> str:
        return str(pd.DataFrame({i: j for i, j in zip(self.__head, self.__data)}, index=[0]))


class History:
    def __init__(self, product, category, quantity, value, entry_exit):
        self.__product = product
        self.__category = category
        self.__quantity = quantity
        self.__value = value
        self.__entry_exit = entry_exit
        self.__date = datetime.datetime.now().date().strftime('%m-%d-%Y')

    def get_product(self):
        return self.__product

    def get_category(self):
        return self.__category

    def get_quantity(self):
        return self.__quantity

    def get_value(self):
        return self.__value

    def get_date(self):
        return self.__date

    def entry_exit(self):
        return self.__entry_exit

    def __str__(self) -> str:
        return f'      Produto: {self.__product}\n' \
               f'    Categoria: {self.__category}\n' \
               f'   Quantidade: {self.__quantity}\n' \
               f'        Valor: {self.__value}\n' \
               f'         Data: {self.__date}' \
               f'Entrada/saida: {self.__entry_exit}'

    def __repr__(self) -> str:
        return f'({self.__product}, ' \
               f'{self.__category}, ' \
               f'{self.__entry_exit}, ' \
               f'{self.__quantity}, ' \
               f'{self.__value}, ' \
               f'{self.__date})'