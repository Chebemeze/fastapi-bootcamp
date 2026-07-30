def error_hint(error_type):
    if not error_type:
        return

    match error_type:
        case "NameError":
            return "Check variable names and spelling."
        case "TypeError":
            return "Check the types before using an operator."
        case "ValueError":
            return "Check whether the value can be converted."
        case "ZeroDivisionError":
            return "Check that the denominator is not zero."
        case "IndexError":
            return "Check the index is inside the valid range."

        # handles any other error_type entered by the a user
        case _:
            return "Read the traceback carefully."