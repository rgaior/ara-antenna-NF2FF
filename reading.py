from struct import *
import numpy as np

# def timestepreader(filename):
#     field = []
#     with open(filename, 'rb') as f:
#         while True:
#             thefloatbin = f.read(4)  
#             thefloat = unpack('f',thefloatbin)
#             field.append(thefloat)

#     return field

def timestepreader(filename):
    field = np.array([])
    f = open(filename, 'rb')
    for i in range(1):
        thefloatbin = f.read(4)  
        thefloat = unpack('f',thefloatbin)
        field = np.append(field,thefloat)

    f.close()
    return field
