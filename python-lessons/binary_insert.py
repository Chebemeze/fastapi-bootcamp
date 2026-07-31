class CupNode:
    def __init__(self, price):
        self.price = price
        self.left = None
        self.right = None

def insert_node(node, price):
    if node is None:
        return CupNode(price)
    
    if price < node.price:
        node.left = insert_node(node.left, price)
    elif price > node.price:
        node.right = insert_node(node.right, price)

#test case to test the insert function in python
root = CupNode(4.00)
insert_node(root, 3.00)
insert_node(root, 5.00)

print(root.left.price)
print(root.right.price)