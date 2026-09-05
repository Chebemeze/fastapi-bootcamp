def analyze_survey(responses):
    tally = {}
    # TODO: loop through `responses` and populate `tally`
    for color in responses:
        tally[color]= tally.get(color, 0)+1

    if not tally:
        return {"tally": {}, "most_popular": None}

    most_popular = None
    highest_count = 0
    first_appearance = False
    # TODO: loop through `tally` to find the color with the highest count
    # (keep the first one seen in case of a tie)
    for color, n_appearance in tally.items():
        if n_appearance > highest_count:
            highest_count = n_appearance
        if highest_count == n_appearance and not first_appearance:
            most_popular = color
            first_appearance = True
    return {"tally": tally, "most_popular": most_popular}
