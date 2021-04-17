from time import sleep

class TrafficLight:
    __color = ''

    def running(self):
        for i in range(10):
            self.__color = 'Green'
            print(self.__color)
            sleep(7)

            self.__color = 'Yellow'
            print(self.__color)
            sleep(2)

            self.__color = 'Red'
            print(self.__color)
            sleep(6)


a = TrafficLight()
a.running()
