def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y

print(max_of_two(25, 62))

def max_of_three(x, y, z):
    if x > (y and z):
        return x
    elif y > (x and z):
        return y
    elif z > (x and y):
        return z
    else:
        return x

print(max_of_three(3, 3, 3))
