class Exception:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

         while True:
            try:
                val = input('Введите число и нажмите Enter (stop - остановка) - ')
                if val.isdigit():
                    self.my_list.append(val)
                    print(f'Текущий список - {self.my_list} \n ')
                else:
                    if val == 'stop':
                        print(self.my_list)
                        break
                    else:
                        raise

            except:
                print(f"Недопустимое значение - строка и булево")


try_except = Exception(1)
print(try_except.my_input())