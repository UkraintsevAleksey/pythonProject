class Data:
    def __init__(self, data):
        self.day_month_year = data

    @classmethod
    def unpack(cls, day_month_year):
        my_list = []

        for i in day_month_year.split('-'):
            my_list.append(i)

        return int(my_list[0]), int(my_list[1]), int(my_list[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 2000:
                    return f'Date is valid!'
                else:
                    return f'Date {day}/{month}/{year} invalid! Year must be between 2000...2021'
            else:
                return f'Date {day}/{month}/{year} invalid! Month between 1...12!'
        else:
            return f'Date {day}/{month}/{year} invalid! Day between 1...31!'

    def __str__(self):
        return f'Current date is {Data.unpack(self.day_month_year)}'


today = Data('11-1-2001')
print(today)
print(Data.valid(2, 11, 2021))
print(today.valid(12, 12, 1999))
print(Data.unpack('11 - 11 - 2011'))
print(today.unpack('11 - 11 - 2020'))
print(Data.valid(12, 8, 2001))