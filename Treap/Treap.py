import random
import math

class Treap:
    def __init__(self):
        self.root = None
    

    def Insert(self, key, priority = None):
        #Empty tree
        if not self.root:
            self.root = TreapNode(key)
            if priority:
                self.root.priority = priority
            return self.root
        current, Prev = self.root, None
        
        #Find Insertion point
        while current:
            if key < current.key:
                current, prev = current.left, current
            else:
                current, prev = current.right, current

        #Insert node
        node = TreapNode(key)
        if priority:
            node.priority = priority
        if key < prev.key:
            node.parent, prev.left = prev, node
        else:
            node.parent, prev.right = prev, node

        #Balance
        current = prev
        while current:
            if current.left and current.left.priority > current.priority:
                self.__RightRotate(current)
                current = current.parent.parent
            elif current.right and current.right.priority > current.priority:
                self.__LeftRotate(current)
                current = current.parent.parent
            else:
                current = None
        return node

    def Remove(self, node):
        #Rotate the node down to a leaf
        while node.left or node.right:
            #Note, extra cases for easier-to-read logic
            if not node.right:
                self.__RightRotate(node)
            elif not node.left:
                self.__LeftRotate(node)
            elif node.left.priority > node.right.priority:
                self.__RightRotate(node)
            else:
                self.__LeftRotate(node)

        #Cut leaf node
        if node.parent and node == node.parent.left:
            node.parent.left = None
        elif node.parent and node == node.parent.right:
            node.parent.right = None
        else:
            self.root = None


    #Special Operations

    def Split(self, key):
        node = self.Insert(key, math.inf)
        left, right = Treap(), Treap()
        left.root, right.root = node.left, node.right
        node.left.parent, node.right.parent = None, Nonew
        return (left, right)

    def Join(self, other):
        #note, other is assumed greater 
        root, oroot = self.root, other.root
        node = TreapNode(0)
        node.left, node.right, root.parent, oroot.parent = root, oroot, node, node
        self.Remove(node)

    def SearchAndAdjust(self, k):
        #Not sure this makes sense, I found some notes that this might be neat
        node = self.Search(k)
        node.priority = max(node.priority, random.randint(0, 1000))
        current = node.parent
        while current:
            if current.left and current.left.priority > current.priority:
                self.__RightRotate(current)
                current = current.parent.parent
            elif current.right and current.right.priority > current.priority:
                self.__LeftRotate(current)
                current = current.parent.parent
            else:
                current = None
        return node

    def FingerSearch(self, f, k):
        if not f.parent:
            return self.Search(k)
        v, current = f.parent, None
        c = 0
        while True:
            c += 1
            #Upwards step
            if v:
                if v.key <= f.key:
                    v = v.parent
                elif f.key < v.key and v.key <= k:
                    v, current = v.parent, v
                else:
                    v, current = None, v
            

            #Downwards step
            if current:
                if current.key == k:
                    print(c,' search steps')
                    return current
                elif k < current.key:
                    current = current.left
                else:
                    current = current.right



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
            self.left, self.right, self.parent, self.key, self.priority = None, None, None, key, random.randint(0, 1000)

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
                    else:
                        raise Exception("Node not found")
            elif command.startswith('split'):
                for t in tree.Split(command.split()[1]):
                    print(t)
            elif command.startswith('join'):
                ntree = Treap()
                for i in command.split()[1:]:
                    ntree.Insert(i)
                tree.Join(ntree)
            elif command.startswith('adjust'):
                for i in command.split()[1:]:
                    tree.SearchAndAdjust(i)
            elif command.startswith('finger'):
                for i in command.split()[1:]:
                    left, right = i.split('-')
                    print(tree.FingerSearch(tree.Search(left), right).key)
            elif command.startswith('print'):
                print(tree)
        except EOFError:
            break

if __name__ == '__main__':
    main()
