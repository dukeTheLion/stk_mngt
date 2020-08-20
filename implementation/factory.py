from entities.management import Stock, History
from datebase.DB import Table
import pandas as pd


class StockFactory:
    def __init__(self):
        self.__path = 'Tabelas/Estoque.csv'
        self.__file = Table(self.__path)

    def get_table(self):
        return self.__file.get_table()

    def exit(self, obj):
        tb1 = self.__file.get_table()
        tb2 = obj.get_data()

        find = tb1.loc[tb1['Produto'].isin([tb2[0]])].index.tolist()[0]
        rest = tb1.loc[find].tolist()[-2] - obj.get_data()[-2]

        tb2[-2] = obj.get_data()[-2] = rest if rest > 0 else 0

        if find is []:
            tb1.add_tb(obj)
        else:
            tb1.update_tb(find[0], obj)
