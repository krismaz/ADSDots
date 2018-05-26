import random
import math

class SplayTree:
    def __init__(self):
        self.root = None
    

    def Insert(self, key):
        node = self.Search(key)
        if node:
            return node
        node = SplayTreeNode(key)
        if self.root and self.root.key < key:
            node.left = self.root
            node.right = self.root.right
            self.root.right = None
            node.left.parent = node
            if node.right:
                node.right.parent = node
        elif self.root and self.root.key >= key:
            node.right = self.root
            node.left = self.root.left
            self.root.left = None
            node.right.parent = node
            if node.left:
                node.left.parent = node
        self.root = node
        return node

    def Remove(self, node):
        self.Splay(node)
        if not node.left and not node.right:
            self.root = None
        elif not node.left:
            self.root = node.right
            self.root.parent = None
        elif not node.right:
            self.root = node.left
            self.root.parent = None
        else:
            self.root = node.left
            self.root.parent = None
            self.Splay(self.Maximum())
            self.root.right = node.right
            node.right.parent = self.root 

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

    def Splay(self, x):
        while True:
            y = x.parent
            if not y:
                break
            z = y.parent
            if not z:
                #zig
                if x == y.left:
                    self.__RightRotate(y)
                else:
                    self.__LeftRotate(y)
            elif x == y.left and y == z.left:
                #zig-zig
                self.__RightRotate(z)
                self.__RightRotate(y)
            elif x == y.right and y == z.right:
                #zig-zig
                self.__LeftRotate(z)
                self.__LeftRotate(y)
            elif x == y.right and y == z.left:
                #zig-zig
                self.__LeftRotate(y)
                self.__RightRotate(z)
            elif x == y.left and y == z.right:
                #zig-zig
                self.__RightRotate(y)
                self.__LeftRotate(z)
            else:
                raise Exception("Programming err")
        self.root = x


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


class SplayTreeNode:
    def __init__(self, key):
            self.left, self.right, self.parent, self.key = None, None, None, key

def main():
    tree =  SplayTree()
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
