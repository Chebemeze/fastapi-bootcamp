names = ["Ada", "Chidi", "Ada", "Nkem", "Chidi", "Chidi", "Femi", "Nkem", "Ada"]

# --- Get unique attendees (messy nested-loop approach) ---
unique_names = []
for name in names:
    is_duplicate = False
    for existing in unique_names:
        if name == existing:
            is_duplicate = True
    if not is_duplicate:
        unique_names.append(name)

print("Unique attendees:", unique_names)

# --- Count duplicate check-ins (repeats the same nested-loop pattern) ---
duplicate_count = 0
seen_for_dupes = []
for name in names:
    already_seen = False
    for existing in seen_for_dupes:
        if name == existing:
            already_seen = True
    if already_seen:
        duplicate_count += 1
    else:
        seen_for_dupes.append(name)

print("Duplicate check-ins:", duplicate_count)

# --- Find most called name (yet another nested-loop pattern) ---
most_called = ""
highest_count = 0
checked_names = []
for name in names:
    if name in checked_names:
        continue
    checked_names.append(name)
    count = 0
    for other in names:
        if other == name:
            count += 1
    if count > highest_count:
        highest_count = count
        most_called = name

print("Most called name:", most_called)


# YOUR REFACTORED VERSION GOES BELOW
# Requirements:
#   - get_unique_attendees(names)
#   - count_duplicate_checkins(names)
#   - most_called_name(names)
# Must use dict/set logic, no nested loops, identical printed output.

def get_unique_attendees(names):
    new_list = list(dict.fromkeys(names))
    return new_list

def count_duplicate_checkins(names):
    new_list = {}
    for i in names:
        new_list[i] = new_list.get(i, 0)+1
    total = 0
    for key, value in new_list.items():
        if value > 1:
            total += value-1
    return total

def most_called_name(names):
    new_dict = {}
    for i in names:
        new_dict[i] = new_dict.get(i,0)+1
    max_item = max(new_dict, key=new_dict.get)
    return max_item
