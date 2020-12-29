class Data:

    @classmethod
    def get_data(self, str_dmy):
        day = int(str_dmy[0:2])
        month = int(str_dmy[3:5])
        year = int(str_dmy[6:len(str_dmy)])

        return day, month, year

    @staticmethod
    def check_data(str_dmy):
        if int(str_dmy[0:2]) < 0 or int(str_dmy[0:2]) > 31 or int(str_dmy[3:5]) < 0 or int(str_dmy[3:5]) > 12 or int(str_dmy[6:len(str_dmy)]) < 0:
            print('Некорректный формат даты!')
        else:
            print('Корректный формат даты!')

my_str = '30-08-2019'

print(Data.get_data(my_str))
print(Data.check_data(my_str))
