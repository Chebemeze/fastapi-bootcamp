import sys

number_list = []
print("Using a normal list")
def get_orders_generator_list(n):
    for i in range(n):
        number_list.append(i)
    return number_list
result = get_orders_generator_list(1000000)
print(f"Memory size: {sys.getsizeof(result)} bytes\n")

print("A case When yield keyword generator is used")
#applying the yield keyword generator
def get_orders_generator(n):
    for i in range(n):
        yield f"Order #{i}"

# Instantly returns a generator object using almost zero memory
massive_gen = get_orders_generator(1000000)
print(f"Memory size: {sys.getsizeof(massive_gen)} bytes")

print("\nAnother example\n")
# Another example. The difference between a pre allocated memory and a lazy generator
list_comp = [x * x for x in range(10000)] #allocaetes memory
gen_expr = (x * x for x in range(10000)) # creates a lazy generator
print("List comp size:", sys.getsizeof(list_comp), "bytes")
print("Gen expr size:", sys.getsizeof(gen_expr), "bytes")

print("\nAnother example\n")
#Another example
def infinite_coffee_stream():
    order_id = 1
    drinks = ['Latte', 'Mocha', 'Cappuccino']
    while True:
        # Cycle through the drinks list based on the order ID
        drink = drinks[order_id % len(drinks)]
        yield {
            'id': order_id,
            'drink': drink,
            'price': 4.50 + (order_id % 2) * 0.50
        }
        order_id += 1

# Process the first 3 orders from our infinite stream
stream = infinite_coffee_stream()
print(next(stream))  # Order 1
print(next(stream))  # Order 2
print(next(stream))  # Order 3

print("\nAnother example\n")
#Another example
def order_generator(limit):
    for i in range(1, limit + 1):
        yield f"Order #{i}"

for order in order_generator(3):
    print(order)

print("\nAnother example using yield from\n")
def morning_shift():
    yield "Espresso"
    yield "Latte"

def afternoon_shift():
    yield "Mocha"
    yield "Iced Coffee"

def full_day_menu():
    yield from morning_shift()    # Delegates directly to the sub-generator
    yield from afternoon_shift()  # Delegates directly to the sub-generator

for drink in full_day_menu():
    print("Serving:", drink)


# How to pipe generators together
def order_source():
    # Simulate a database stream of raw orders
    yield {'id': 1, 'drink': 'latte', 'price': 4.50}
    yield {'id': 2, 'drink': 'mocha', 'price': 5.00}
    yield {'id': 3, 'drink': 'espresso', 'price': 3.50}

def apply_tax_pipeline(stream):
    # This generator modifies prices lazily as they pass through
    for order in stream:
        order['price_with_tax'] = order['price'] * 1.10
        yield order

def receipt_formatter(stream):
    # This generator formats the modified orders
    for order in stream:
        yield f"Order #{order['id']}: {order['drink'].capitalize()} — ₦{order['price_with_tax']:.2f}"

# Chain the generators together!
raw_orders = order_source()
taxed_orders = apply_tax_pipeline(raw_orders)
receipts = receipt_formatter(taxed_orders)

for receipt in receipts:
    print(receipt)