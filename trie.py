# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
    """A node in the Trie"""
    __slot__ = ['value', 'children', 'complete', 'count']

    def __init__(self, val):
        """Create a node and possible children from a word fragment"""
        self.children = {}
        self.count = 0
        self.complete = False
        
        if not val:
            return
        
        self.value = val[0]
        if len(val) > 1:
            self.children = {val[1] : Node(val[1:])}
        else:
            self.complete = True
        self.count = 1
        

class Trie:
    """Trie for contacts"""
    root = None
    
    def __init__(self):
        self.root = Node('')

    def add(self, contact):
        node = self.root
        for i, char in enumerate(contact):
            if char in node.children:
                node = node.children[char]
                node.count += 1
            else:
                node.children[char] = Node(contact[i:])
                break
                
        if node != self.root:
            node.complete = True
    
    def _find(self, contact):
        node = self.root
        for char in contact:
            if char in node.children:
                node = node.children[char]
            else:
                return 0
        return node
    
    def find(self, contact):
        node = self._find(contact)
        if node:
            print(node.count)
        else:
            print(0)


n = int(input().strip())
contacts = Trie()

for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        contacts.add(contact)
    if op == 'find':
        contacts.find(contact)
