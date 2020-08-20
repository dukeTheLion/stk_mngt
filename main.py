from datebase.DB import Table
import csv
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


add = pd.DataFrame({'Produto': ['h', 'i', 'C'],
                    'Categoria': ['NUM', 'NUM', 'NUN'],
                    'Entrada/Saida': ['Entrada', 'Entrada', 'Entrada'],
                    'Data de registro': ['10-2-19', '10-2-19', '10-2-19'],
                    'Quantidade': [1, 2, 2],
                    'Valor/kg': [23.56, 23.56, 34]})

k = Table('Tabelas/Historico - cópia.csv')


