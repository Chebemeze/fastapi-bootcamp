def access_gate(age, has_id, is_banned):
    if age < 18:
        return "Too young"
    if not has_id:
        return "No ID"
    if is_banned:
        return "Banned"
    return "Allowed"
