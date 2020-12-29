class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data = input("Введите делимое: ")
inp_data_2 = input("Введите делитель: ")

try:
    inp_data = int(inp_data)
    inp_data_2 = int(inp_data_2)
    if inp_data_2 == 0:
        raise OwnError("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Результат деления: {inp_data / inp_data_2}")