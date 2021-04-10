def my_pow_funс(x, y):
    try:
        res = x ** y
    except TypeError:
        return "TypeError!"
    return res

print(my_pow_funс(2, 0))

