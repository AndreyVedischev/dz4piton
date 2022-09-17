# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141

def pi():
    k = 1
    s = 0
    for i in range(1000000):
        if i % 2 == 0:
            s += 4 / k
        else:
            s-= 4 /k
        k += 2
    return s

p = str(pi())
print(p[:5])