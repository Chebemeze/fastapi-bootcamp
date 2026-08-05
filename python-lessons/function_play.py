def add(x):
    def sum(y):
        return x*y
    return sum

a = add(3)
for i in range(1, 13):
    print(f"{i} * 3 = {a(i)}\n")