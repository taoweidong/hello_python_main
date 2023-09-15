_variable = 1


def test():
    global _variable
    _variable = 2


test()
print(_variable)
