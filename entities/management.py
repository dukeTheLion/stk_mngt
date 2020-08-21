import pandas as pd
import datetime


class Stock:
    def __init__(self, product, category,  quantity, value, data=datetime.datetime.now().date().strftime('%m-%d-%Y')):
        self.__head = ['Produto', 'Categoria', 'Data de registro', 'Quantidade', 'Valor/kg']
        self.__data = [product, category, data, quantity, value]

    def get_head(self):
        return self.__head

    def get_data(self):
        return self.__data

    def __str__(self) -> str:
        return str(pd.DataFrame({i: j for i, j in zip(self.__head, self.__data)}, index=[0]))


class History:
    def __init__(self, product, category, quantity, value, entry_exit):
        self.__head = ['Produto', 'Categoria', 'Entrada/Saida', 'Data de registro', 'Quantidade', 'Valor/kg']
        self.__data = [product, category, entry_exit, datetime.datetime.now().date().strftime('%m-%d-%Y'),
                       quantity, value]

    def get_product(self):
        return self.__head

    def get_category(self):
        return self.__data

    def __str__(self) -> str:
        return str(pd.DataFrame({i: j for i, j in zip(self.__head, self.__data)}, index=[0]))
