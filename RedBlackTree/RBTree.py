# RedBlackTree, stright outa Cormen
class RedBlackTree:
    def __init__(self):
        self.root = None
    
    # RBtree helpers
    def __isBlack(self, node):
        if not node:
            return True
        return not node.red

    def __isRed(self, node):
        return node and node.red

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

    def __RBTransplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def Insert(self, key):
        y = None
        x = self.root
        z = RedBlackNode(key)
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if not y:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = z.right = None
        z.red = True
        self.__RBInsertFixup(z)
        return z

    def __RBInsertFixup(self, z):
        while z.parent and z.parent.red:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if self.__isRed(y):
                    z.parent.red = False
                    y.red = False
                    z.parent.parent.red = True
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.__LeftRotate(z)
                    z.parent.red = False
                    z.parent.parent.red = True
                    self.__RightRotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if self.__isRed(y):
                    z.parent.red = False
                    y.red = False
                    z.parent.parent.red = True
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.__RightRotate(z)
                    z.parent.red = False
                    z.parent.parent.red = True
                    self.__LeftRotate(z.parent.parent)
        self.root.red = False

    def Sibling(self, node):
        if node == node.parent.left:
            return node.parent.right
        return node.parent.right

# FML http://stackoverflow.com/questions/6723488/red-black-tree-deletion-algorithm
    def Remove(self, node):
        if not node.right or not node.left:
            y = node
        else:
            y = self.Successor(node)
        if y.left:
            x = y.left
        else:
            x = y.right
        if x:
            x.parent = y.parent
        xParent = y.parent

        if not y.parent:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
            left = True
        else:
            y.parent.right = x
            left = False
        if y != node:
            node.key = y.key
        if not y.red:
            self.Fix(x, xParent, left)

    def Fix(self, x, parent, left):
        while x != self.root and self.__isBlack(x):
            if left:
                w = parent.right
                if self.__isRed(w):
                    w.red = False
                    parent.red = True
                    self.__LeftRotate(parent)
                    w = parent.right
                if self.__isBlack(w.left) and self.__isBlack(w.right):
                    w.red = True
                    x = parent
                    parent = x.parent
                    left = parent and x == parent.left
                else:
                    if self.__isBlack(w.right):
                        w.left.red = False
                        w.red = True
                        self.__RightRotate(w)
                        w = parent.right
                    w.red = parent.red
                    parent.red = False
                    if w.right:
                        w.right.red = False
                    self.__LeftRotate(parent)
                    x = self.root
                    parent = None
            else:
                w = parent.left
                if self.__isRed(w):
                    w.red = False
                    parent.red = True
                    self.__RightRotate(parent)
                    w = parent.left
                if self.__isBlack(w.left) and self.__isBlack(w.right):
                    w.red = True
                    x = parent
                    parent = x.parent
                    left = parent and x == parent.left
                else:
                    if self.__isBlack(w.left):
                        w.right.red = False
                        w.red = True
                        self.__LeftRotate(w)
                        w = parent.left
                    w.red = parent.red
                    parent.red = False
                    if w.left:
                        w.left.red = False
                    self.__RightRotate(parent)
                    x = self.root
                    parent = None
        if x:
            x.red = False

    #BSTree Methods, move when we get a new one
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
        return 'graph RBTree{\n' + '\n'.join(bunch) + '\n}'

    def __PrintEdges(self, id, parent, node, bunch):
        if not node:
            return id
        id = id + 1
        if node.red:
            bunch.append('node_' + str(id) + '[label="' + str(node.key) + '" fillcolor="#FFAAAA" style="filled"];')
        else:
            bunch.append('node_' + str(id) + '[label="' + str(node.key) + '" fillcolor="#AAAAAA" style="filled"];')
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


class RedBlackNode:
    def __init__(self, key):
            self.left, self.right, self.parent, self.key, self.red = None, None, None, key, True

def main():
    tree =  RedBlackTree()
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
