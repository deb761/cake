import re

instr = '2+2*3-1'
operators = ['*', '/', '+', '-']

class Node:
    left = None
    right = None
    operator = None
    parent = None
    def __init__(self, left, toks, parent=None):
        self.left = left
        self.operator = toks.pop(0)
        self.right = int(toks.pop(0))
        self.parent = parent
        if toks:
            self.right = Node(self.right, toks, self)

    def __str__(self):
        return '{} {} {}'.format(self.left, self.operator, self.right)


def doop(operator, left, right):
    if operator == '+':
        return left + right
    if operator == '-':
        return left - right
    if operator == '*':
        return left * right
    return left / right


toks = re.split('([*/+-])', instr)

left = int(toks.pop(0))
node = Node(left, toks)

# work backwards through the nodes
while isinstance(node.right, Node):
    node = node.right


while node.parent:
    prec = operators.index(node.operator)
    par_prec = operators.index(node.parent.operator)
    if par_prec < prec:
        node.left = doop(node.parent.operator,
                         node.parent.left,
                         node.left)
        node.parent = node.parent.parent
    if node.parent:
        node.parent.right = doop(node.operator, node.left, node.right)
        node = node.parent

print(doop(node.operator, node.left, node.right))
