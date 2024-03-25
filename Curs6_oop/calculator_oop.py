class Calculator:

    def __init__(self):
        self.operator_1 = float(input('Alege primul numar: '))
        self.semn = input('Alege operatia: ')
        self.operator_2 = float(input('Alege al doilea numar: '))
        while not self.operator_2 and self.semn == '/':
            self.operator_2 = float(input('Alege al doilea numar: '))

    def adunare(self):
        return self.operator_1 + self.operator_2

    def scadere(self):
        return self.operator_1 - self.operator_2

    def inmultire(self):
        return self.operator_1 * self.operator_2

    def impartire(self):
        return self.operator_1 / self.operator_2

    def __str__(self):
        if self.semn == '+':
            return f'{self.operator_1} {self.semn} {self.operator_2} = {self.adunare()}'
        elif self.semn == '-':
            return f'{self.operator_1} {self.semn} {self.operator_2} = {self.scadere()}'
        elif self.semn == '*':
            return f'{self.operator_1} {self.semn} {self.operator_2} = {self.inmultire()}'
        elif self.semn == '/':
            return f'{self.operator_1} {self.semn} {self.operator_2} = {self.impartire()}'
        else:
            return 'Operatia nu exista'


obj_calculator = Calculator()
print(obj_calculator)
