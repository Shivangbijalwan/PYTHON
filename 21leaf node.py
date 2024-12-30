class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.index = -1

    def build_tree(self, nodes):
        self.index += 1
        if self.index >= len(nodes) or nodes[self.index] == -1:
            return None

        new_node = Node(nodes[self.index])
        new_node.left = self.build_tree(nodes)
        new_node.right = self.build_tree(nodes)
        return new_node

    def print_leaf_nodes(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            print(node.data, end=" ")
        self.print_leaf_nodes(node.left)
        self.print_leaf_nodes(node.right)

if __name__ == "__main__":
    nodes = [1, 2, 4, -1, 5, -1, -1, 3, -1, 6, -1, -1]
    tree = BinaryTree()
    root = tree.build_tree(nodes) 
    tree.print_leaf_nodes(root)