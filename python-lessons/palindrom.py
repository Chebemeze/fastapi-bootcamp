
#returns true if the word is a palindrom else returns false
def manual_palindrome(text):
    if text is not None:
        if not text.isdigit():
            cleaned_text = text.strip().lower()
            len_text = len(cleaned_text)
            new_str = ""
            for x in range(len_text):
                new_str = new_str + cleaned_text[len_text-1-x]
            if new_str == cleaned_text:
                return True
            else:
                return False
