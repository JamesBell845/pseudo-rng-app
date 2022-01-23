import json



def normaliser(value):
    """
    want to end up with a number between 1 and 10000
    """
    if value > 10000:
        while value > 10000:
            value *= 0.75
    elif value < 1:
        while value < 1:
            value *= 10

    value = int(value)
    return value




def number_generator(date):
    value = 1

    return value


if __name__ == "__main__":
    date = "2021/12/24"

    print(number_generator(date))
