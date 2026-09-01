def make_change(amount_owed_cents, amount_paid_cents):
    #deal with error case first
    if amount_paid_cents < amount_owed_cents:
        raise ValueError("Insufficient payment")
    
    #calculate the change that will be given back
    change_due = amount_paid_cents - amount_owed_cents

    #preparing a default dictionary where all values are set to zero
    dict_of_cents = {25: 0, 10: 0, 5: 0, 1: 0}

    for key,_ in dict_of_cents.items():
        if (change_due // key) != 0:
            # performing floor division to know how many denomination in cents makes up
            #change due
            quarter = change_due // key

            #dict_of_cents[key] is the number of times key(denomination) makes up change_due
            #without remaainder
            dict_of_cents[key] = quarter
            
            #updates change_due so the next denominatin(key) can perform accurate
            change_due -= key
        else:
            #this ensures that we move to a denomination the new change_due is greater than
            # key here is the denominations. ensures that calculations are only done
            if change_due < key:
                continue
    return dict_of_cents

res = make_change(50, 80)
print(res)