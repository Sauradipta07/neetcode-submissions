class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        # Dummy nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove a node from the linked list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Insert a node immediately before tail
    # This means the node becomes the MRU
    def insert(self, node):
        prev = self.tail.prev
        next = self.tail

        node.prev = prev
        node.next = next

        prev.next = node
        next.prev = node

    def get(self, key: int) -> int:

        # Key doesn't exist
        if key not in self.map:
            return -1

        # Get the node
        node = self.map[key]

        # It was just used, so make it MRU
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.map:
            node = self.map[key]

            # Update value
            node.value = value

            # Mark as recently used
            self.remove(node)
            self.insert(node)

        else:
            # Create a new node
            node = Node(key, value)

            # Store it in hashmap
            self.map[key] = node

            # Add it as MRU
            self.insert(node)

            # Cache exceeded capacity
            if len(self.map) > self.capacity:

                # LRU node is right after dummy head
                lru = self.head.next

                # Remove from linked list
                self.remove(lru)

                # Remove from hashmap
                del self.map[lru.key]