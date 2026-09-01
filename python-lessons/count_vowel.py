def count_vowels(text):
    vowels = "aeiou"
    count = 0
    # TODO: loop through `text`, check each character (case-insensitively)
    # against `vowels`, and increment `count` when it matches
    if text is None:
        return 0
    lower_case_text = text.lower()
    for alpha_bet in lower_case_text:
        if alpha_bet.isdigit():
            continue
        for j in vowels:
            if alpha_bet == j:
                count += 1
    return count

count = count_vowels("Sky")
print(count)