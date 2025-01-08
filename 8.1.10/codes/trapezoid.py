import ctypes
lib = ctypes.CDLL('./trapezoid.so')
lib.Area.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int]
lib.Area.restype = ctypes.c_double

ll = -1 # value of a
ul = 2.0 # value of b
n = 1000 # Subintervals

print("Area bounded is: ",lib.Area(ll, ul, n))
