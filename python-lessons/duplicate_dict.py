def replica(a):
    b = set()
    c = {}
    for key, value in a.items():
        if key not in b:
            b.add(key)
            c[key]=value
    return c

res = replica({"Rice": 2, "beans": 9, "Rice":4,})
print(res)
