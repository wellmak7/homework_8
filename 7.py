class Complex:

    def __init__(self, complex_num):
        self.complex_num = complex_num

    def __add__(self, other):
        try:
            if "+" in self.complex_num:
                self.real_part_self = int(self.complex_num[:self.complex_num.find("+")])
                try:
                    self.imagine_part_self = int(self.complex_num[self.complex_num.find("+"):(len(self.complex_num)-1)])
                except ValueError:
                    self.imagine_part_self = 1
            else:
                self.real_part_self = int(self.complex_num[:self.complex_num.find("-")])
                try:
                    self.imagine_part_self = int(self.complex_num[self.complex_num.find("-"):(len(self.complex_num) - 1)])
                except ValueError:
                    self.imagine_part_self = -1

            if "+" in other.complex_num:
                self.real_part_other = int(other.complex_num[:other.complex_num.find("+")])
                try:
                    self.imagine_part_other = int(other.complex_num[other.complex_num.find("+"):(len(other.complex_num)-1)])
                except ValueError:
                    self.imagine_part_other = 1
            else:
                self.real_part_other = int(other.complex_num[:other.complex_num.find("-")])
                try:
                    self.imagine_part_other = int(other.complex_num[other.complex_num.find("-"):(len(other.complex_num) - 1)])
                except ValueError:
                    self.imagine_part_other = -1

            self.real_part = self.real_part_self + self.real_part_other
            self.imagine_part = self.imagine_part_self + self.imagine_part_other

            if self.imagine_part < 0:
                self.sign = "-"
            else:
                self.sign = "+"

            print(f'Результат сложения комплексных чисел: {self.real_part} {self.sign} {abs(self.imagine_part)}i')
        except ValueError:
            print("Введено не комплексное число!")

    def __mul__(self, other):
        try:
            if "+" in self.complex_num:
                self.real_part_self = int(self.complex_num[:self.complex_num.find("+")])
                try:
                    self.imagine_part_self = int(self.complex_num[self.complex_num.find("+"):(len(self.complex_num)-1)])
                except ValueError:
                    self.imagine_part_self = 1
            else:
                self.real_part_self = int(self.complex_num[:self.complex_num.find("-")])
                try:
                    self.imagine_part_self = int(self.complex_num[self.complex_num.find("-"):(len(self.complex_num) - 1)])
                except ValueError:
                    self.imagine_part_self = -1

            if "+" in other.complex_num:
                self.real_part_other = int(other.complex_num[:other.complex_num.find("+")])
                try:
                    self.imagine_part_other = int(other.complex_num[other.complex_num.find("+"):(len(other.complex_num)-1)])
                except ValueError:
                    self.imagine_part_other = 1
            else:
                self.real_part_other = int(other.complex_num[:other.complex_num.find("-")])
                try:
                    self.imagine_part_other = int(other.complex_num[other.complex_num.find("-"):(len(other.complex_num) - 1)])
                except ValueError:
                    self.imagine_part_other = -1

            self.real_part = self.real_part_self * self.real_part_other + self.imagine_part_self * self.imagine_part_other * (-1)
            self.imagine_part = self.real_part_self * self.imagine_part_other + self.real_part_other * self.imagine_part_self

            if self.imagine_part < 0:
                self.sign = "-"
            else:
                self.sign = "+"

            print(f'Результат умножения комплексных чисел: {self.real_part} {self.sign} {abs(self.imagine_part)}i')
        except ValueError:
            print("Введено не комплексное число!")

num_1 = Complex("1-i")
num_2 = Complex("3+6i")

num_1 + num_2
num_1 * num_2

