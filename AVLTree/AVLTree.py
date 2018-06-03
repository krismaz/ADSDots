import random
import math

class AVLTree:
    def __init__(self):
        self.root = None
    

    def Insert(self, key):
       pass

    def Remove(self, node):
        pass

    def Search(self, key, start=None):
        if not start:
            start = self.root
        while start and key != start.key:
            if key < start.key:
                if not start.left:
                    self.Splay(start)
                    return
                start = start.left
            else:
                if not start.right:
                    self.Splay(start)
                    return
                start = start.right
        if start:
            self.Splay(start)
        return start


    #Utility
    def __LeftRotate(self, node):
        y = node.right
        node.right = y.left
        if y.left:
            y.left.parent = node
        y.parent = node.parent
        if not node.parent:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:# node == node.parent.right:
            node.parent.right = y
        y.left = node
        node.parent = y
        self.__FixHeight(node)
        self.__FixHeight(y)

    def __RightRotate(self, node):
        x = node.left
        node.left = x.right
        if x.right:
            x.right.parent = node
        x.parent = node.parent
        if not node.parent:
            self.root = x
        elif node == node.parent.right:
            node.parent.right = x
        else: #if node == node.parent.left:
            node.parent.left = x
        x.right = node
        node.parent = x
        self.__FixHeight(node)
        self.__FixHeight(x)



    def __FixHeight(self, node):
        node.height = 1
        if node.left and node.left.height >= node.height:
            node.height = node.left.height + 1
        if node.right and node.right.height >= node.height:
            node.height = node.right.height + 1 
   
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
        bunch.append('node_' + str(id) + '[label="{' + str(node.key) + '}"];')
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


class AVLTreeNode:
    def __init__(self, key):
            self.left, self.right, self.parent, self.key, self.height = None, None, None, key, 1

def main():
    tree =  AVLTree()
    command = ''
    while True:
        try:
            command = input()
            if command.startswith('insert'):
                for i in command.split()[1:]:
                    tree.Insert(i)
            if command.startswith('search'):
                for i in command.split()[1:]:
                    tree.Search(i)
            elif command.startswith('remove'):
                for i in command.split()[1:]:
                    node = tree.Search(i, None)
                    if node:
                        tree.Remove(node)
                    else:
                        raise Exception("Node not found")
            elif command.startswith('print'):
                print(tree)
        except EOFError:
            break

if __name__ == '__main__':
    main()
