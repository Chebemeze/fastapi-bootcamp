def delivery_fee(order_total, distance_km, is_member):
    if order_total < 0 or distance_km < 0:
        return "Invalid input"
    if is_member and order_total >= 5000:
        return 0

    if distance_km <= 5:
        return 500
    elif distance_km <= 15:
        return 1000
    else:
        return 2000
