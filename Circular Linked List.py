class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.last = None

    def addToEmpty(self, data):
        if self.last != None:
            return self.last

        newNode = Node(data)

        self.last = newNode

        self.last.next = self.last
        return self.last

    def addFront(self, data):

        if self.last == None:
            return self.addToEmpty(data)

        newNode = Node(data)

        newNode.next = self.last.next

        self.last.next = newNode

        return self.last

    def addEnd(self, data):
        # Check if the node is empty
        if self.last == None:
            return self.addToEmpty(data)

        newNode = Node(data)

        newNode.next = self.last.next

        self.last.next = newNode

        self.last = newNode

        return self.last


    def addAfter(self, data, item):


        if self.last == None:
            return None

        newNode = Node(data)
        m = self.last.next
        while m:

            if m.data == item:

                newNode.next = m.next

                m.next = newNode

                if m == self.last:
                    self.last = newNode
                    return self.last
                else:
                    return self.last
            m = m.next
            if m == self.last.next:
                print(item, "The given node is not present in the list")
                break

    def deleteNode(self, last, key):

        # If linked list is empty
        if last == None:
            return

        if (last).data == key and (last).next == last:

            last = None

        temp = last
        m = None

        if (last).data == key:

            while temp.next != last:
                temp = temp.next

            temp.next = (last).next
            last = temp.next

        while temp.next != last and temp.next.data != key:
            temp = temp.next

        if temp.next.data == key:
            d = temp.next
            temp.next = d.next

        return last

    def traverse(self):
        if self.last == None:
            print("The list is empty")
            return

        newNode = self.last.next
        while newNode:
            print(newNode.data, end=" ")
            newNode = newNode.next
            if newNode == self.last.next:
                break

# Driver Code
if __name__ == "__main__":

    CLL = CircularLinkedList()
    last = CLL.addToEmpty(3)
    last = CLL.addEnd(8)
    last = CLL.addFront(9)
    last = CLL.addAfter(12, 3)

    CLL.traverse()

    last = CLL.deleteNode(last, 8)
    print()
    CLL.traverse()
