""" This function checks if a string passed in through the variable text
have equal brackets and are in order. Brackets include (, ), {, }, [, and ]
"""

def is_balanced(text):
    """ 
        Args:
            text: a string passed so the function can check if it's ballanced.
        
        Return:
            Boolean: it returns True if text is a ballanced string and False if it's not ballanced
        
        Example:
            >>> from bracket_checker import is_balanced
            >>> value = is_balanced("")
            >>> print(value)
                True
            >>> value = is_balanced("(")
            >>> print(value)
                False
            >>> value = is_balanced("()")
            >>> print(value)
                True
            >>> value = is_balanced("({)]")
            >>> print(value)
                False
            >>> value = is_balanced("You've gotten this far, you can now copy the code")
            >>> print(value)
                True
            >>> value = is_balanced("Feel free to buy me coffee")
            >>> print(value)
                True
    """
    # TODO: return True if all brackets in `text` are properly matched and nested,
    # False otherwise. Ignore non-bracket characters.

    if text is None:
        return True
    if text.isalpha():
        return True
    
    #there are two operations:
    #1. the number of character that they matched then count them
    #2. check the order of appearance
    dict_of_characters = {}
    only_brackets_string = ""
    for i in text:
        if i.isalpha():
            continue

        only_brackets_string += i

        if i == "}" or i == ")" or i == "]":
            if i == "}":
                i = "{"
            elif i == ")":
                i = "("
            elif i == "]":
                i = "["
            
        dict_of_characters[i] = dict_of_characters.get(i, 0) + 1

    #checks if text doesn't contain any bracket
    check = ["(", ")", "{", "}", "[", "]"]
    no_bracket = False
    for j in range(len(text)):
        for p in range(len(check)):
            if check[p] == text[j]:
                no_bracket = True
        if no_bracket:
            break

    # If text doesn't contain any brackets it returns True meaning it is ballanced
    if not no_bracket:
        return True

    #Handles if the number of brackets match
    for key, value in dict_of_characters.items():
        if value % 2 != 0:
            return False

    length_of_string = len(only_brackets_string)
    num_of_runs = int(length_of_string/2)
    next_num = length_of_string - 1

    #handles the order by comparing only bracket string by index to see if they are in order
    dict_of_acceptable_bracket = {")": "(", "}": "{", "]": "["}
    for i in range(num_of_runs):
        key_to_find = only_brackets_string[next_num]
        if only_brackets_string[i] == dict_of_acceptable_bracket[key_to_find]:
            next_num -= 1
        else:
            return False
    return True
