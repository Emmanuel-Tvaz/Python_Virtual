import math
def run():
    # super_dict = {
    #     "natural_nums" : [1,2,3,4,5],
    #     "integer_nums" : [-1,-2,0,1,2],
    #     "floating_nums" : [1.1,4.5,5.43]
    # }

    dict = {}

    #Crear diccionario con las llaves de 1 al 100 que no sean divisibles entre 3 y
    #  cuyo valor sea la llave elevada al cubo
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         dict[i]= i**3
    # print(dict)

    #Dictionary Comprehensions.py
    # my_dict = {i : i ** 3 for i in range(0,101) if i % 3 != 0}
    # print(my_dict)

    my_dict_example = {i: math.sqrt(i)  for i in range(1,1000) }
    print(my_dict_example)

if __name__ == "__main__":
    run()