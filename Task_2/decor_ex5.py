
def validate(*val_types):
    def decorator(func):
        def wrap(*args):
            i = 0
            for types in val_types:
                val = args[i]
                if not isinstance(val, types):
                    raise TypeError(f"type a expected: {types}, but got {type(val)}")
                i = i + 1
            return func(*args)

        return wrap

    return decorator


@validate((int, float), (list, tuple), (int, float))
def func(a: int | float, b: list | tuple, c: int | float) -> list:
    pass


@validate((list, tuple), (list, tuple), (int, float))
def func2(a, b, c) -> list:
    pass


@validate((int, float), (int, float), (int, float), (int, float), (int, float))
def func3(a, b, c, d, e) -> list:
    pass


@validate((int, float), (list, tuple), (int, float), (int, float), (list, tuple))
def func4(a, b, c, d, e):
    pass


# decorator = validate()
# wrap = decorator(func)
# print(wrap(1, 2))

#  func3(1, 2, 3, 4)
func4(1, [2], 3, 2, [3])
