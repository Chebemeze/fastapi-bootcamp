CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "1234"
username_found, username_attempt, password_attempt = False, 0, 0

while True:
    if username_attempt == 4 or password_attempt == 4:
        print("Account locked.")
        break
    if not username_found:

        username = input("Enter username: ")
    if username != CORRECT_USERNAME:
        if username_attempt < 3:
            print("Incorrect username. Try again.")
        username_attempt += 1
    else:
        username_found = True
        password = input("Enter password: ")
        if password != CORRECT_PASSWORD:
            if password_attempt < 3:
                print("Incorrect password. Try again.")
            password_attempt += 1
        else:
            print("Login successful!")
            break
