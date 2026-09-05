def items_to_restock(current_stock, minimum_levels):
    # TODO: loop through current_stock, compare against minimum_levels,
    # and return a list of item names below their minimum
    needs_restocking = []
    for item, quantity in current_stock.items():
        if item in minimum_levels:
            if quantity < minimum_levels[item]:
                needs_restocking.append(item)
    return needs_restocking
