import random

class Treap:
    def __init__(self):
        self.root = None
    

    def Insert(self, key):
        raise Exception("NOTIMPL")

    def Remove(self, node):
       raise Exception("NOTIMPL")

   
    #Tree Methods, move when we get a new one
    def Minimum(self, start=None):
        if not start:
            start = self.root
        if not start:
            return None
        while start.left:
            start = start.left
        return start

    def Maximum(self, start=None):
        if not start:
            start = self.root
        if not start:
            return None
        while start.right:
            start = start.right
        return start

    def Search(self, key, start=None):
        if not start:
            start = self.root
        while start and key != start.key:
            if key < start.key:
                start = start.left
            else:
                start = start.right
        return start

    def Successor(self, node):
        if node.right:
            return self.Minimum(node.right)
        y = node.parent
        while y and node == y.right:
            node = y
            y = y.parent
        return y

    def InOrder(self):
        start = self.Minimum()
        while start:
            yield start
            start = self.Successor(start)

    # Printing and stuff
    def __str__(self):
        bunch = []
        self.__PrintEdges(0, 0, self.root, bunch)
        return 'graph Treap{\nnode [shape=record];\n' + '\n'.join(bunch) + '\n}'

    def __PrintEdges(self, id, parent, node, bunch):
        if not node:
            return id
        id = id + 1
        bunch.append('node_' + str(id) + '[label="{' + str(node.key) +' | ' + str(node.priority) +'}"];')
        if node.parent and not node.parent.right:
            bunch.append('node_' + str(parent) + ':sw -- node_' + str(id) + ';')
        elif node.parent and  not node.parent.left:
            bunch.append('node_' + str(parent) + ':se -- node_' + str(id) + ';')
        elif node.parent:
            bunch.append('node_' + str(parent) + ' -- node_' + str(id) + ';')
        next = id
        if node.left:
            next = self.__PrintEdges(id, id, node.left, bunch)
        if node.right:
            next = self.__PrintEdges(next, id, node.right, bunch)
        return next


class TreapNode:
    def __init__(self, key):
            self.left, self.right, self.parent, self.key, self.priority = None, None, None, key, None

def main():
    tree =  Treap()
    command = ''
    while True:
        try:
            command = input()
            if command.startswith('insert'):
                for i in command.split()[1:]:
                    tree.Insert(i)
            elif command.startswith('remove'):
                for i in command.split()[1:]:
                    node = tree.Search(i, None)
                    if node:
                        tree.Remove(node)
            elif command.startswith('print'):
                print(tree)
        except EOFError:
            break

if __name__ == '__main__':
    main()
