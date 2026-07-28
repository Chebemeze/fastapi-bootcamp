# def square(x):
#     return x * x

# print(square(5))
# print("After applying lambda:")

# numbers = [8,2,3,4,5]
# a = (x*x for x in numbers)
# print(list(a))
# print(next(a))

# # lambda
# a = filter(lambda x: x%2 == 0, numbers)
# b = sorted(numbers)
# print(b)

cart = [{"item": "cup", "qty": 10}, {"item": "spoon", "qty": 3}]
sorted_cart = sorted(cart, key=lambda x: x["qty"])
print(sorted_cart)