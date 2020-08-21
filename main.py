from entities.factory import StockFactory
from entities.management import Stock
import pandas as pd

"""app = QApplication(sys.argv)
print(f'{app.primaryScreen().size().height()}')"""

"""table = pd.read_csv('Tabelas/Historico.csv')

add = pd.DataFrame({'Produto': ['h', 'i'],
                    'Categoria': ['NUM', 'NUM'],
                    'Entrada/Saida': ['Entrada', 'Entrada'],
                    'Data de registro': ['10-2-19', '10-2-19'],
                    'Quantidade': [1, 2],
                    'Valor/kg': [23.56, 23.56]})

table = table.append(add)

valor = add.to_csv(header=False, index=False)
print(valor)

with open('Tabelas/Historico - cópia.csv', 'a') as acv:
    acv.write( + valor)"""

"""add = pd.DataFrame({'Produto': ['h', 'i', 'C'],
                    'Categoria': ['NUM', 'NUM', 'NUN'],
                    'Entrada/Saida': ['Entrada', 'Entrada', 'Entrada'],
                    'Data de registro': ['10-2-19', '10-2-19', '10-2-19'],
                    'Quantidade': [1, 2, 2],
                    'Valor/kg': [23.56, 23.56, 34]})"""

"""add = [Stock('k', 'NUM', 10, 21.50),
       Stock('t', 'NUM', 7, 20.0),
       Stock('y', 'NUM', 20, 30.50),
       Stock('v', 'NUM', 15, 1.50)]


head = Table('Tabelas/Estoque.csv').get_head()
lista = [[], [], [], [], []]

for i in add:
    lista[0].append(i.get_product())
    lista[1].append(i.get_category())
    lista[2].append(i.get_date())
    lista[3].append(i.get_quantity())
    lista[4].append(i.get_value())

dic = dict(zip(head, lista))

print(dic)"""


"""obj = StockFactory('Tabelas/Estoque.csv')

print(obj.get_table())

obj.exit(['C', 'NUN', '10-2-19', 2.0, 34.00])"""


"""obj = Stock('G', 'NUM', 10, 10.5)

StockFactory().exit(obj)
"""
"""
new = pd.DataFrame(columns=['Produto', 'Categoria', 'Data de registro', 'Quantidade', 'Valor/kg'])
new = new.append({j: i for i, j in zip(['C', 'NUN', '10-2-19', 2.0, 34.00], new.columns)}, ignore_index=True)
new = new.append({j: i for i, j in zip(['C', 'NUN', '10-2-19', 2.0, 34.00], new.columns)}, ignore_index=True)
new = new.append({j: i for i, j in zip(['C', 'NUN', '10-2-19', 2.0, 34.00], new.columns)}, ignore_index=True)
print(new)"""

with open('Tabelas/Estoque.csv', 'r') as archive:
    for i in archive.readlines():
        print(i.split(','))

#new = StockFactory()

#new.add(Stock('K', 'NUM', 10, 10.5))

