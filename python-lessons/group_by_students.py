def group_by_grade(students):
    # TODO: determine each student's letter grade and group their names by grade band
    new_dict = {}
    for i in students:
        if i["score"] >= 90:
            grade = "A"
        elif 80<=i["score"]<=89:
            grade = "B"
        elif 70<= i["score"]<=79:
            grade = "C"
        elif 60<= i["score"]<=69:
            grade = "D"
        elif i["score"]<60:
            grade= "F"

        if grade in new_dict:
            new_dict[grade].append(i["name"])
        else:
            new_dict[grade] = [i.get("name")]

    return new_dict
print(group_by_grade([{"name": "Ada", "score": 92}, {"name": "Bola", "score": 95}]))
