class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # empty list and one element list
        if self.head == None or self.head.get_next() == None:
            pass
        else: # for multiple element lists
            # creating a new list starting with the head
            currently_working_on = self.head
            next_to_work_on = self.head.get_next()
            self.head = Node(currently_working_on.get_value()) # cant just add to head becasue that would retain the old list still
            currently_working_on = next_to_work_on
            # looping through the rest of the list
            while currently_working_on != None:
                next_to_work_on = currently_working_on.get_next()
                self.add_to_head(currently_working_on.get_value())
                currently_working_on = next_to_work_on
            

        # multiple element list
        
            
