def smart_title_case(sentence):
    # TODO: capitalize each word except connector words (a, an, the, of, in, on, and),
    # unless that connector word is the first word in the sentence
    except_ions = ["a", "an", "the","of", "in", "on", "and"]
    new_sentence = ""
    capital = False
    for i in sentence:
        if i != " " and not capital:
            upper_case = i.upper()
            new_sentence += upper_case
            capital = True
        else:
            new_sentence += i
   
        if i == " ":
            capital = False
    # new_sentence is now sentence with first letters of all words capitalized

    #This second part handles anywhere the words in except_ions appear
    #in sentence except if it is found at the beginning of the sentence

    splited_words = new_sentence.split()

    #I used splitted_words[1:] to avoid the first word in splitted words
    index = 1
    for j in splited_words[1:]:
        if j.lower() in except_ions:
            splited_words[index] = j.lower()
        index += 1
    return " ".join(splited_words)

print(smart_title_case("a good way to kickstart this. the greatest showman of this generation is in the building and is performing on stage"))