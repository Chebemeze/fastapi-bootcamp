# Exploring strict FILO using built append() in a manager class

#this defines what each node should contain. attribute name and a pointer to another node
class CupNode:
    def __init__(self, name):
        self.name = name
        self.next = None


#this manages the Cupnode and ensures a strict FILO when append() is used
class ManagerNode:
    def __init__(self):
        self.head = None
    
    def append(self, name):
        new_cup = CupNode(name)
        if self.head == None: #when the node is empty
            self.head = new_cup
            return
        
        #if the first node is not empty, current which will serve as the traversial variable should point to the first node
        current = self.head

        #This loop helps us to check each node ensuring that the new cup will not be appended to a None node
        while current.next is not None:
            current = current.next
        
        current.next = new_cup # linking the new cup to the last cup

# test case to test the node and node manager
bluecup = ManagerNode()
bluecup.append("Red")
bluecup.append("Orange")
bluecup.append("Yellow")
bluecup.append("Green")
bluecup.append("Blue")
bluecup.append("Indigo")
bluecup.append("Violet")

current = bluecup.head
while current.next is not None:
    print(current.name)
    current = current.next

