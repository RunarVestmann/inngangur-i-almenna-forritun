# Mutable
# list, set, dictionary

# The list will change outside the function
def list_function(some_list):
    some_list.append(4)

# The set will change outside the function
def set_function(some_set):
    some_set.add(4)

# The dictionary will change outside the function
def dict_function(some_dict):
    some_dict["some_key"] = "some_value"



# Immutable
# string, int, float, tuple

# If we want to change a string, int, float or a tuple with a function
# we need to return a new instance and 
# override the original when we receive the value from the function

def string_function(name):
    return name.lower()

def int_function(some_int):
    return some_int + 4

def float_function(some_float):
    return some_float + 3.14

def tuple_function(some_tuple):
    return ("A", "new", "tuple")

