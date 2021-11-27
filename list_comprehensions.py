def run():
    # squares = []
    # for i in range (0,101):
    #     if i % 3 != 0:    
    #         squares.append(i**2)

    #Imprime el cuadrado de los números del 1 al 100 que no son divisibles entre 4
    squares = [i**2 for i in range(0,101) if i % 4 != 0]
    print(squares)

    #Todos los multiplos de 4 que tambien es  múltiplo de 6 y 9
    multiples = [i for i in range(0,100000) if i % 36 ==0]
    print(multiples)
if __name__ == "__main__":
    run()