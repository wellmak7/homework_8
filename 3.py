class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []

while True:
    inp_data = input("Введите очередной элемент списка: ")

    try:
        if inp_data == 'stop':
            print(my_list)
            break
        else:
            inp_data = int(inp_data)
            my_list.append(inp_data)

    except ValueError:
        # raise OwnError("Нужно ввести число!")
        print("Нужно ввести число!")
    except OwnError as err:
        print(err)