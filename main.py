class Resistor:
    def __init__(self, c):
        self.c = c
        self.cd = {'black': 0,
                   'brown': 1,
                   'red': 2,
                   'orange': 3,
                   'yellow': 4,
                   'green': 5,
                   'blue': 6,
                   'violet': 7,
                   'gray': 8,
                   'white': 9,
                   'gold': '5%',
                   'silver': '10%'
                   }

    def get_res(self):
        """
        Метод, що повертає значення опору резистора на основі його колірного коду.

        Returns:
        float: Значення опору резистора в омах.

        """
        fr = self.cd[self.c[0]]
        sr = self.cd[self.c[1]]
        if len(self.c) >= 3:
            thr = self.cd[self.c[2]]
            r = (fr * 10 + sr) * (10 ** thr)
        else:
            r = (fr * 10 + sr)
        if len(self.c) >= 4:
            if self.c[3] == 'gold':
                r *= 0.1
            elif self.c[3] == 'silver':
                r *= 0.01
            else:
                r *= 0.1 ** self.cd[self.c[3]]
        if len(self.c) >= 5:
            r *= 0.1 ** self.cd[self.c[4]]
        if len(self.c) == 6:
            r *= 0.1 ** self.cd[self.c[5]]
        return r

    def get_tol(self):
        """
        Метод, що повертає значення допустимої похибки резистора на основі його колірного коду.

        Returns:
        str: Значення допустимої похибки резистора у відсотках.

        """
        if len(self.c) >= 4:
            if self.c[-1] == 'gold':
                t = '5%'
            elif self.c[-1] == 'silver':
                t = '10%'
            else:
                t = str(self.cd[self.c[-1]]) + '%'
        else:
            t = None
        return t


if __name__ == "__main__":
    resistor = Resistor(['brown', 'black', 'red', 'orange'])
    print('Опір резистора:', resistor.get_res(), 'Ом')
    print('Допустима похибка:', resistor.get_tol())
