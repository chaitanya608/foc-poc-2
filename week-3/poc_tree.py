"""
Python definition of basic Tree class
"""


class Tree:
    """
    Recursive definition for tree plus various tree methods
    """

    def __init__(self, value, children):
        """
        Create a tree whose root has specific value (a string)
        children is a list of references to the roots of the children
        """
        self._value = value
        self._children = children

    def __str__(self):
        """
        Generate a string representation of the tree.
        Use a pre-order traversal of the tree.
        """
        ans = "["
        ans += str(self._value)

        for child in self._children:
            ans += ", "
            ans += str(child)

        return ans + "]"

    def get_value(self):
        """
        Getter for node's value
        """
        return self._value

    def children(self):
        """
        Generator to return children
        """
        for child in self._children:
            yield child

    def num_nodes(self):
        """
        Compute number of nodes in the tree
        """
        ans = 1
        for child in self._children:
            ans += child.num_nodes()

        return ans

    def num_leaves(self):
        """
        Compute number of leaves in the tree
        """
        ans = 1
        for child in self._children:
            if child.num_nodes() == 0:
                ans += 1

        return ans

    def height(self):
        """
        Compute height of a tree rooted by self
        """
        height = 0  # height is 0 when root has no children
        for child in self._children:
            height = max(height, child.height() + 1)

        return height


def run_examples():
    """
    Create some trees and apply various methods to these trees
    """
    tree_a = Tree("a", [])
    tree_b = Tree("b", [])
    print("Tree consisting of single leaf node labelled 'a'", tree_a)
    print("Tree consisting of single leaf node labelled 'b'", tree_b)

    tree_cab = Tree("c", [tree_a, tree_b])
    print("Tree consisting of three nodes: ", tree_cab)

    tree_dcabe = Tree("d", [tree_cab, Tree("e", [])])
    print("Tree consisting of five nodes: ", tree_dcabe)
    print()

    my_tree = Tree("a", [
        Tree("b", [
            Tree("c", []), Tree("d", [])
        ]),
        Tree("e", [
            Tree("f", [
                Tree("g", [])
            ]),
            Tree("h", []),
            Tree("i", [])
        ])
    ])
    print("Tree with nine nodes", my_tree)

    print("The tree has", my_tree.num_nodes(), "nodes.")
    print("with", my_tree.num_leaves())
    print("and height of", my_tree.height())


run_examples()
