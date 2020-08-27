from entities.management import History


class StockFactory:
    def __init__(self):
        self.__path = 'Tabelas/Estoque.csv'

    def add(self, obj):
        temp = []

        with open(self.__path, 'r') as archive:
            for i in archive.readlines():
                temp.append(i.split(','))

        equal = [i for i in temp if i[0] == obj.get_product()]
        oppst = [i for i in temp if i[0] != obj.get_product()]

        if equal:
            result = round(float(equal[0][3]), 2) + float(obj.get_quantity())
            equal[0][3] = str(result)
            equal[0][4] = str(obj.get_value())
            oppst.append(equal[0])

            with open(self.__path, 'w') as archive:
                for i in oppst:
                    archive.write(','.join(i))

            HistoryFactory().add(obj)

        else:
            with open(self.__path, 'a') as archive:
                archive.write('\n' + ','.join([str(i) for i in [obj.get_product(),
                                                                obj.get_category(),
                                                                obj.get_data(),
                                                                obj.get_quantity(),
                                                                obj.get_value()]]))
            HistoryFactory().add(obj)

    def exit(self, obj):
        temp = []

        with open(self.__path, 'r') as archive:
            for i in archive.readlines():
                temp.append(i.split(','))

        equal = [i for i in temp if i[0] == obj.get_product()]
        oppst = [i for i in temp if i[0] != obj.get_product()]
        result = 0

        if not equal:
            print('Produto não previamente incluso no estoque')
            return

        if equal:
            result = float(equal[0][3]) - float(obj.get_quantity())
            equal[0][3] = str(result) if result >= 0 else '0'

        if equal and result > 0:
            oppst.append(equal[0])

        with open(self.__path, 'w') as archive:
            for i in oppst:
                archive.write(','.join(i))

        HistoryFactory().exit(obj)


class HistoryFactory:
    def __init__(self):
        self.__path = 'Tabelas/Historico.csv'

    def add(self, obj):
        add = History(obj.get_product(), obj.get_category(), obj.get_quantity(), obj.get_value(), True)
        with open(self.__path, 'a') as archive:
            archive.write('\n')
            archive.write(','.join([add.get_product(),
                                    add.get_category(),
                                    add.get_entry_exit(),
                                    add.get_data(),
                                    add.get_quantity(),
                                    add.get_value()]))

    def exit(self, obj):
        add = History(obj.get_product(), obj.get_category(), obj.get_quantity(), obj.get_value(), False)
        with open(self.__path, 'a') as archive:
            archive.write('\n')
            archive.write(','.join([add.get_product(),
                                    add.get_category(),
                                    add.get_entry_exit(),
                                    add.get_data(),
                                    add.get_quantity(),
                                    add.get_value()]))
