
#returns true if the word is a palindrom else returns false
def manual_palindrome(text):
    if text is not None:
        if not text.isdigit():
            cleaned_text = text.strip().lower()
            delimeter = [",", "*"," ", ".", "-"]
            #loop removes any of the five delimeter listed above. further cleans the text
            for y in delimeter:
                cleaned = cleaned_text.split(y)
                cleaned_text = "".join(cleaned)

            len_text = len(cleaned_text)
            new_str = ""
            #forms a new string backward from the cleaned text
            for x in range(len_text):
                new_str = new_str + cleaned_text[len_text-1-x]
            
            #handling comparison of both strings
            if new_str == cleaned_text:
                return True
            else:
                return False
