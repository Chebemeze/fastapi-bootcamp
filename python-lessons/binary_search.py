from binary_insert import insert_node, CupNode

#search function
def searchNode(node, target):
    if node is None:
        return node
    if node.price == target:
        return node
    
    if target < node.price:
        return searchNode(node.left, target)
    elif target > node.price:
        return searchNode(node.right, target)

start_node = CupNode(5)

#inserts into the node first
insert_node(start_node, 3)
insert_node(start_node, 6)
insert_node(start_node, 10)

#checks if 5 is in the node so we can print
found = searchNode(start_node, 5)
print(found.price)

#checks what gets printed when we use a number not in the node
missing = searchNode(start_node, 8)
print(missing)

