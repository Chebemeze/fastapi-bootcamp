def initials_badge(full_name):
    #handle when full_name is empty or whitespaces
    if not full_name or not full_name.strip():
        return
    words = full_name.strip().title().split()
    initial = [word[0] for word in words]
    return ".".join(initial) + "."