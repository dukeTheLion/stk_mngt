class StockFactory:
    def __init__(self):
        self.__path = 'Tabelas/Estoque.csv'

    def add(self, obj):
        with open(self.__path, 'a') as archive:
            archive.write('\n' + ','.join([str(i) for i in obj.get_data()]))

    def exit(self, obj):
        with open(self.__path, 'a') as archive:
            return
