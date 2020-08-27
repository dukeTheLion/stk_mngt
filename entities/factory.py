class StockFactory:
    def __init__(self):
        self.__path = 'Tabelas/Estoque.csv'

    def add(self, obj):
        temp = []

        with open(self.__path, 'r') as archive:
            for i in archive.readlines():
                temp.append(i.split(','))

        equal = [i for i in temp if i[0] == obj.get_data()[0]]
        oppst = [i for i in temp if i[0] != obj.get_data()[0]]

        if equal:
            result = round(float(equal[0][3]), 2) + obj.get_data()[3]
            equal[0][3] = str(result)
            equal[0][4] = str(obj.get_data()[4])
            oppst.append(equal[0])

            with open(self.__path, 'w') as archive:
                for i in oppst:
                    archive.write(','.join(i))

        else:
            with open(self.__path, 'a') as archive:
                archive.write('\n' + ','.join([str(i) for i in obj.get_data()]))

    def exit(self, obj):
        temp = []

        with open(self.__path, 'r') as archive:
            for i in archive.readlines():
                temp.append(i.split(','))

        equal = [i for i in temp if i[0] == obj.get_data()[0]]
        oppst = [i for i in temp if i[0] != obj.get_data()[0]]
        result = 0

        if equal:
            result = float(equal[0][3], ) - obj.get_data()[3]
            equal[0][3] = str(result) if result >= 0 else '0'

        if equal and result > 0:
            oppst.append(equal[0])

        with open(self.__path, 'w') as archive:
            for i in oppst:
                archive.write(','.join(i))


class HistoryFactory:
    def __init__(self):
        self.__path = 'Tabelas/Historico.csv'

    def add(self):
        return

    def exit(self):
        return
