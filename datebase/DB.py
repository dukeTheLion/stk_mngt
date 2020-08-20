from csv import writer
import pandas as pd


class Table:
    def __init__(self, path, ch=False):
        self.__appd = None
        self.__path = path
        self.__ch = ch

        self.table = self.__open_tb()
        self.tb_head = self.table.columns.tolist()

    def __open_tb(self):
        self.table = pd.read_csv(self.__path)
        return self.table

    def __warning(self):
        temp_tb = self.table.append(self.__appd, ignore_index=True)
        duplicate = temp_tb.duplicated()[temp_tb.index.max() - self.__appd.index.max():]
        index = [i for i in range(self.__appd.index.max() + 1) if duplicate.tolist()[i]]
        rows = self.__appd.loc[index]

        if len(rows) != 0:
            chr = ''
            for i in self.tb_head:
                chr += i + '  '

            x = round(len(chr) * 0.333)
            drt1 = ' ' * x + '+' + '-' * 21 + '+'
            drt2 = ' ' * x

            print(f'{drt1}\n{drt2}|  Linhas duplicadas  |\n{drt1}')
            print(rows)
            print('\n\nDeseja manter?(s/n)')

            while True:
                swr = input('').lower()

                if swr == 's':
                    return
                elif swr == 'n':
                    self.__appd = self.__appd.drop(index)
                    return
                else:
                    print('\nResposta invalida. Deseja manter?(s/n)')

    def save_tb(self):
        if self.__appd is not None:
            self.__warning()

            if self.__ch:
                apd_tb = self.__appd.to_csv(index=False)

                with open(self.__path, 'a') as archive:
                    archive.write('\n' + apd_tb)

            if not self.__ch:
                new_tb = self.table.append(self.__appd).to_csv(index=False)

                with open(self.__path, 'w') as archive:
                    archive.write(new_tb)

    def update_tb(self, rows):
        if self.tb_head == rows.columns.tolist():
            if self.__appd is None:
                self.__appd = rows
            else:
                self.__appd.append(rows, ignore_index=True)

