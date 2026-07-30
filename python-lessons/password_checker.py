def password_strength(password):
    password_len = len(password)
    
    if password_len < 8:
        return "Weak"
    elif password_len >= 8 and password.isalpha() and not password.isdigit():
        return "Medium"
    elif  password_len >= 8 and password.isdigit() and not password.isalpha():
        return "Medium"
    elif password_len >= 8:
        #first loop checks if there is at least one digit in the password
        for x in password:
            if x.isdigit():
                is_digit = True
                break
        # second loop checks if there is at least one alphabet in the password
        for y in password:
            if y.isalpha():
                is_alpha = True
                break
        if is_alpha and is_digit:
            return "Strong"

status = [password_strength("abc12"), password_strength("abcdefgh"), password_strength("abc12345")]
print(status)
