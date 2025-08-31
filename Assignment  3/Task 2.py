import math
n = int(input("Enter a number: "))

def cal(n):
    square = math.sqrt(n)
    print("Square Root: ",square)
    log = math.log(n)
    print("Logarithm: ",log)
    sin = math.sin(n)
    print("Sine: ",sin)

cal(n)