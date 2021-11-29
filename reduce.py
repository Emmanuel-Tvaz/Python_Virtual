def run():
    from functools import reduce
    my_list = [2,2,2,2,2]

    multiplied = reduce(lambda a, b : a * b, my_list)
    print(multiplied)

if __name__ == "__main__":
    run()