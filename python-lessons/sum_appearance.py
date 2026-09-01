def find_sum(stocks):
    dict_of_quantity = {}
    dict_of_count = {}

    for item, quantity in stocks:
        dict_of_quantity[item] = dict_of_quantity.get(item, 0)+quantity
        dict_of_count[item] = dict_of_count.get(item, 0)+1

    decision_list = {key: value for key, value in dict_of_count.items() if value >1}

    if decision_list is None:
        return {}

    final_dict = {}
    for key in decision_list:
        final_dict[key] = final_dict.get(key, dict_of_quantity[key])

    return final_dict


stocks = [("Rice", 10), ("Beans", 3), ("Bread", 10), ("Rice", 5), ("Bread", 8), ("Bread", 9)]
res = find_sum(stocks)
print(res)