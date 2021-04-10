def div(s_1, s_2):

        s_1, s_2 = int(s_1), int(s_2)
        if s_2 == 0:
            print('Error! Div zero division!')
        else:
            div_num = s_1 / s_2
        return round(div_num, 2)

print(div(input('Enter first figure - '), input('Enter second figure -')))
