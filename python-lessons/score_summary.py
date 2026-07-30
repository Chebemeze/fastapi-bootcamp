def score_summary(name, a, b, c):
    try:
        score_a = int(a)
        score_b = int(b)
        score_c = int(c)
    except ValueError:
        return "Invalid score"
    
    scores = [score_a, score_b, score_c]
    score_bool = [True for x in scores if 0>x>100]
    for val in list(score_bool):
        if val == True:
            return "Invalid score"
    average_score = (score_a + score_b + score_c)/3
    average_s = round(average_score, 2)
    if average_s >= 90:
        grade = "A"
    elif average_s >= 80:
        grade = "B"
    elif average_s >= 70:
        grade = "C"
    elif average_s < 70:
        grade = "F"
    
    return f"Student: {name}\nAverage: {average_s}\nGrade: {grade}"
