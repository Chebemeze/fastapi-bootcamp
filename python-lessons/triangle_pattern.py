def triangle_pattern(n):
    if n < 1 :
        return ""
    new_string = ""
    for i in range(1,n+1):
        for j in range(i):
            new_string += "*"
        if n > 1 and i != n: 
            new_string += "\n"
    return new_string
