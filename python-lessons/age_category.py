def age_category(age):
    #handles when no age is passed
    if not age:
        return
    if age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"
