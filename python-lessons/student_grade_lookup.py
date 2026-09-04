def get_student_grade(students, name):
    if len(students) == 0 or name is None:
        return "Not found"
    # TODO: loop through `students` and populate `lookup` with name -> grade
    for i in students:
        lookup = {}
        for key, value in i.items():
            lookup[key]= lookup.get(key, value)
        if lookup["name"] == name:
            return lookup["grade"]
        else:
            continue
    return "Not found"
    # TODO: return the grade for `name` from `lookup`, or "Not found" if missing
