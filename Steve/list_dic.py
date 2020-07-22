def make_dict(**kwargs):
    return kwargs

make_dict(a = 1, b = 2) # returns a dictionary from this

def make_dict(*kwargs):
    return kwargs

make_dict(a = 1, b = 2) # returns a list
