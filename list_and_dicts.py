def run():
    my_list = [1,"hello", True, 4.5]
    my_dict = {"firstname":"Emmanuel","Lastname" : "Torres"}

    super_list = [
        {"firstname":"Emmanuel","Lastname" : "Torres"},
        {"firstname":"Eloisa","Lastname" : "Cruz"},
        {"firstname":"Pablo","Lastname" : "Marmol"},
        {"firstname":"Homero","Lastname" : "Simpson"},
        {"firstname":"Rick","Lastname" : "Sanchez"}
    ]

    super_dict = {
        "natural_nums" : [1,2,3,4,5],
        "integer_nums" : [-1,-2,0,1,2],
        "floating_nums" : [1.1,4.5,5.43]
    }

    for key,value in super_dict.items():
        print(key, "-", value)
    
    for values in super_list:
        for key, value in values.items():
            print (key, ":", value)

    for i in super_list:
        print(i.items())

if __name__ == '__main__':
    run()