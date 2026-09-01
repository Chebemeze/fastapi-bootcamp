users_age = int(input("Age: "))
day = input("Day type (weekday/weekend): ")

if users_age < 5:
    price = 0
    print(f"Price: {price}")
elif 5 <= users_age <= 12:
    if day == "weekday":
        price = 1500
    elif day == "weekend":
        price = 2000
    print(f"Price: {price}")
elif 13 <= users_age <= 59:
    if day == "weekday":
        price = 2500
    elif day == "weekend":
        price = 3500
    print(f"Price: {price}")
elif users_age >= 60:
    if day == "weekday":
        price = 1200
    elif day == "weekend":
        price = 1800
    print(f"Price: {price}")
