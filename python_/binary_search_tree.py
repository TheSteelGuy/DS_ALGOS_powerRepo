"""[In order traversal tree]
"""
from random import randint
class Node:
    """[The Node class here represents individual value added to the tree]
    """
    def __init__(self, value=None):
        #  a node object has a mandatory value and optional two children
        self.value = value 
        self.left_child = None
        self.right_child=None
 

class Binary_search_tree:
    """[the class tree represents the actual tree]
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        """[private recursive method that handles cases that the node object is not root]
        
        Arguments:
            value {[type]} -- [description]
            current_node {[type]} -- [description]
        """
        # check if the value we want to insert is less than current node we are at
        # if so the remember left part of the binary search tree always contains smaller values
        if value < current_node.value:
            # first  we check if there is no value on the left child 
            if current_node.left_child == None:
                current_node.left_child = Node(value)
            # if the current node has a left child then call the function recursively this time with 
            # the left child as the root node
            else:
                self._insert(value, current_node.left_child)
        # we then repeat the same process on the right side of the binary search tree
        elif value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child == Node(value)
            else:
                self._insert(value, current_node.right_child)
        else:
            
            print('Value already in tree')


    def view_tree(self):
        if self.root != None:
            self._view_tree(self.root)

    def _view_tree(self, current_node):
        if current_node != None:
            self._view_tree(current_node.left_child)
            print(current_node.value)
            self._view_tree(current_node.right_child)

def populate_tree(tree):
    for _ in range(100):
        current_node_value = randint(0,1009)
        tree.insert(current_node_value)
     
    return tree

tree = Binary_search_tree()     
tree = populate_tree(tree)

tree.view_tree()

          
# populate_tree(tree)





