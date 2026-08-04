my_list = [1, 2, 3]
my_iterator = iter(my_list)  # Get an iterator from the list

# Check if it has the right methods
print(hasattr(my_list, '__iter__'))    # True - list is iterable
print(hasattr(my_list, '__next__'))    # False - list is NOT an iterator
print(hasattr(my_iterator, '__iter__')) # True - iterator is iterable
print(hasattr(my_iterator, '__next__'))


# Advanced Pattern iterators and state
class OrderProcessor:
    """An iterator that processes orders with custom logic."""
    
    def __init__(self, raw_orders):
        self.raw_orders = raw_orders
        self.index = 0
        self.processed_count = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index >= len(self.raw_orders):
            raise StopIteration
            
        # Get the raw order
        raw = self.raw_orders[self.index]
        self.index += 1
        
        # Process the order (capitalize, add prefix)
        processed = f"CONFERENCE: {raw.upper()}"
        
        # Track statistics
        self.processed_count += 1
        
        return processed
        
    def get_stats(self):
        return {
            'total_processed': self.processed_count,
            'remaining': len(self.raw_orders) - self.index
        }

# Usage
if __name__ == "__main__":
    raw_orders = ['latte', 'mocha', 'cappuccino', 'americano']
    processor = OrderProcessor(raw_orders)

    for order in processor:
        print(order)
        
    print(processor.get_stats())  # {'total_processed': 4, 'remaining': 0}
    