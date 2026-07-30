def vote_eligibility(age, country):
    try:
        age_x = int(age)
    except ValueError:
        return "Enter a valid integer"
    if age_x >= 18 and country.strip().lower() == "nigeria":
        return "Eligible"
    else:
        return "Not eligible"