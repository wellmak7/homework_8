class Storage:
    technic_storage = {}

    def __init__(self, size, color, town):
        self.size = size
        self.color = color
        self.town = town


    def get_technic(self, technic_name, technic_amount):
        self.technic_name = technic_name
        self.technic_amount = technic_amount

        if type(self.technic_amount) is str:
            print("Количество техники должно быть числом!")
        else:
            self.technic_storage[self.technic_name] = self.technic_amount
            print(f'На складе: {self.technic_storage}')

    def move_technic(self, technic_name, technic_amount, subdivision_name):
        self.technic_name = technic_name
        self.technic_amount = technic_amount
        self.subdivision_name = subdivision_name

        if type(self.technic_amount) is str:
            print("Количество техники должно быть числом!")
        else:
            print(f'{self.technic_name} передана в {self.subdivision_name} в количестве {self.technic_amount}')

class Technic:
    def __init__(self, height, width, weight):
        self.height = height
        self.width = width
        self.weight = weight

class Printer(Technic):

    def __init__(self, print_speed):
        self.print_speed = print_speed

class Scaner(Technic):

    def __init__(self, scan_speed, scan_res):
        self.print_speed = print_speed
        self.scan_res = scan_res

class Xerox(Technic):

    def __init__(self, xerox_speed):
        self.xerox_speed = xerox_speed

my_storage = Storage(20, 'white', 'Moscow')

my_storage.move_technic("Пушка", 55, "Склад")
my_storage.get_technic("Машина", 45)
my_storage.get_technic("Холодильник", 50)