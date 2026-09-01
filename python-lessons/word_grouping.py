def group_by_length(words):
    # TODO: return a dict mapping word length to a list of words of that length
    if words is None:
        return {}
    dict_of_words = {}
    for word in words:
        normal_list = []
        word_length = len(word)
        if word_length in dict_of_words:
            dict_of_words[word_length].append(word)
        else:
            normal_list.append(word)
            dict_of_words[word_length] = dict_of_words.get(word_length, normal_list)
    return dict_of_words

words = group_by_length(["a", "b", "c"])
print(words)