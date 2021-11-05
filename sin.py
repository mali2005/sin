import math

def net_degree(degree):
    net = degree%360
    return net

def degree_to_radian(degree):
    tt = 180/degree
    radian = math.pi/tt
    return radian

def sin(degree,count):
    degree = net_degree(degree)
    radian = degree_to_radian(degree)
    alpha = 1
    test = 1
    result = 0
    for i in range(count):
        value1 = math.pow(radian, test)
        value2 = math.factorial(test)
        value = value1/value2
        value = value*alpha
        result += value
        alpha *= -1
        test += 2

    return result

while True:
    a = float(input())
    print(sin(a, 10))
    print("\n")
