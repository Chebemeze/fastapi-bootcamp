def slug_maker(title):
    word = title.lower().strip()
    operator = [" ", ",", "."]
    word_2 = word
    for sign in operator:
        word_1 = word_2.split(sign)
        if type(word_1) is list:
            word_2 = "-".join(word_1)
    final_word = word_2.split("--")
    final_word = "-".join(final_word)
    return final_word
