class Calculator:

    def __init__(self):
        self.operator_1 = self.validate_string(input('Alege primul numar: '))
        self.semn = self.validate_sign(input('Alege operatia: '))
        self.operator_2 = self.validate_string(input('Alege al doilea numar: '))
        while not self.operator_2 and self.semn == '/':
            self.operator_2 = self.validate_string(input('Alege iarasi al doilea numar: '))

    def validate_string(self, input_de_la_tst):
        while not input_de_la_tst.isdigit():
            input_de_la_tst = input('Introduceti corect numarul: ')
        return float(input_de_la_tst)

    @staticmethod
    def validate_sign(semn):
        while semn not in ['+', '-', '*', '/']:
            semn = input("Semnul nu e corect! Alege unul din ['+', '-', '*', '/']")
        return semn

    # def zero_division(self, operator):
    #     while str(operator) in [False, '', '0'] and not str(operator).isdigit():
    #         operator = input('Alege din nou al doilea numar: ')
    #     return float(operator)

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
