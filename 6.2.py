class Road:
    _length = 5000
    _width = 20

    def calculationMassAsphalt(self, massOn1sqM1sm, roadwayThickness):
        print(self._length*self._width*massOn1sqM1sm*roadwayThickness/1000, "т.")

a = Road()
a.calculationMassAsphalt(25, 5)

