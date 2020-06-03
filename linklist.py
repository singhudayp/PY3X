class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
     
    # LinkList Iteration
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    #Add node at First Place
    def add_first(self, node):
        node.next = self.head
        self.head = node

    # Add node in Last
    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    # Add node in between 
    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

########## MAIN PROGRAM #################
#if __name__== "__main__":
#    llist = LinkedList()
#    print(llist)
#    #output : None
#
#    first_node = Node("a")
#    llist.head = first_node
#    print(llist)
#    #output : a -> None
#
#    second_node = Node("b")
#    third_node = Node("c")
#    first_node.next = second_node
#    second_node.next = third_node
#    print(llist)
#    #output : a -> b -> c -> None
#
#    llist = LinkedList(["a", "b", "c", "d", "e"])
#    print(llist)
#    #output : a -> b -> c -> d -> e -> None
#      
#    llist.add_first(Node("0a"))
#    print(llist) 
#    #output : 0a -> a -> b -> c -> d -> e -> None
#
#    llist.add_last(Node("f"))
#    print(llist) 
#    #output : 0a -> a -> b -> c -> d -> e -> f -> None
#
#    llist.add_after("c", Node("cc"))
#    print(llist) 
#    #output : 0a -> a -> b -> c -> cc -> d -> e -> f -> None
#
#    llist.add_after("d", Node("c"))
#    print(llist) 
#    #output : 0a -> a -> b -> c -> cc -> d -> c -> e -> f -> None
#
#    llist.add_after("c", Node("ccd"))
#    print(llist) 
#    #Output : 0a -> a -> b -> c -> ccd -> cc -> d -> c -> e -> f -> None
