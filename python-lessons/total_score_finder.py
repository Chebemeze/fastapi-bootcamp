def total_scores(rounds):
    totals = {}
    for round_scores in rounds:
        for player, points in round_scores.items():
            if player in totals:
                totals[player] += points
            else:
                totals[player] = totals.get(player, points)
    return totals
