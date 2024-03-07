import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return ' -> '.join(elements)

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current:
            data = self.current.data
            self.current = self.current.next
            return data
        else:
            raise StopIteration

# Beispielhafte Verwendung
def main():
    ll = LinkedList()
    
    # Fügen Sie 10 zufällige Zahlen zur Liste hinzu
    for _ in range(10):
        ll.append(random.randint(1, 100))

    print("Elemente in der Liste: ")
    print(ll)
    print("Länge der Liste: ", len(ll))

    print("Elemente der Liste durch Iteration: ")
    for item in ll:
        print(item)

if __name__ == "__main__":
    main()
