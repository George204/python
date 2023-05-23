def find_biggest_float(list_of_floats):
    biggest_float = 0
    for float_number in list_of_floats:
        if float_number > biggest_float:
            biggest_float = float_number
    return biggest_float

def hub_finction(list_of_floats):
    biggest_float = max(list_of_floats)
    return biggest_float

def time_a_function(function, list_of_floats):
    import time
    start = time.time()
    function(list_of_floats)
    end = time.time()
    return end - start

def generate_list_of_random_floats(size):
    import random
    list_of_floats = []
    for i in range(size):
        list_of_floats.append(random.random())
    return list_of_floats



size = 10000000
list_of_floats = generate_list_of_random_floats(size)



print("hub function",time_a_function(hub_finction, list_of_floats))
print("find biggest float",time_a_function(find_biggest_float, list_of_floats))  
input("press enter to exit")