# Read the ISBN string from stdin
isbn_string = input()

def is_valid_isbn_10(isbn):
    # TODO: Implement the validation logic here
    # Check length
    # Check character types
    # Calculate the weighted sum
    # Check divisibility by 11
    if len(isbn) != 10:
        return False

    total = 0
    for index, char in enumerate(isbn):
        multiplier = 10-index
        if index < 9:
            if not char.isdigit():
                return False
            total += multiplier * int(char)
        else:
            if char.lower() == "x":
                total += multiplier * 10
            elif char.isdigit():
                total += multiplier * int(char)
            else:
                return False
    return total%11 == 0

# Print the result
print(is_valid_isbn_10(isbn_string))