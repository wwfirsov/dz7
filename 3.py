class Kletka:
    def __init__(self, kol_kletok):
        self.kol_kletok = kol_kletok

    def __add__(self):
        return self.kol_kletok + self.kol_kletok

    def __sub__(self):
        return self.kol_kletok - self.kol_kletok

    def __mul__(self):
        return self.kol_kletok * self.kol_kletok

    def __truediv__(self):
        return self.kol_kletok / self.kol_kletok

    def make_order(rows, nums):
        return '\n'.join(['*' * rows for _ in range(nums // rows)]) + '\n' + '*' * (nums % rows)

    print(make_order(7, 15))
