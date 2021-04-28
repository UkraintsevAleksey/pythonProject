class Division:
    def __init__(self, divider, dividend):
        self.divider = divider
        self.denominator = dividend

    @staticmethod
    def divide(divider, dividend):
        try:
            return (divider / dividend)
        except:
            return (f"Error! division by zero!")


div = Division(200, 100)
print(Division.divide(12, 0))
print(Division.divide(56, 0.1))
print(div.divide(2, 0))