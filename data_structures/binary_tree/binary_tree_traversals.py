# Import necessary modules and enable Python 3.7+ type hinting
from __future__ import annotations
from collections import deque
from collections.abc import Generator
from dataclasses import dataclass

# Define a Node data structure for a binary tree
@dataclass
class Node:
    data: int
    left: Node | None = None  # Each node has a left child
    right: Node | None = None  # Each node has a right child

# Function to create a sample binary tree
def make_tree() -> Node | None:
    r"""
    The below tree
        1
       / \
      2   3
     / \
    4   5
    """
    # Create a binary tree with the structure shown in the docstring
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    return tree

# Function for pre-order traversal of a binary tree
def preorder(root: Node | None) -> Generator[int, None, None]:
    """
    Pre-order traversal visits root node, left subtree, right subtree.
    """
    if not root:
        return
    yield root.data
    yield from preorder(root.left)
    yield from preorder(root.right)

# Function for post-order traversal of a binary tree
def postorder(root: Node | None) -> Generator[int, None, None]:
    """
    Post-order traversal visits left subtree, right subtree, root node.
    """
    if not root:
        return
    yield from postorder(root.left)
    yield from postorder(root.right)
    yield root.data

# Function for in-order traversal of a binary tree
def inorder(root: Node | None) -> Generator[int, None, None]:
    """
    In-order traversal visits left subtree, root node, right subtree.
    """
    if not root:
        return
    yield from inorder(root.left)
    yield root.data
    yield from inorder(root.right)

# Function for reverse in-order traversal of a binary tree
def reverse_inorder(root: Node | None) -> Generator[int, None, None]:
    """
    Reverse in-order traversal visits right subtree, root node, left subtree.
    """
    if not root:
        return
    yield from reverse_inorder(root.right)
    yield root.data
    yield from reverse_inorder(root.left)

# Function to calculate the height of a binary tree
def height(root: Node | None) -> int:
    """
    Recursive function for calculating the height of the binary tree.
    """
    return (max(height(root.left), height(root.right)) + 1) if root else 0

# Function for level-order traversal of a binary tree
def level_order(root: Node | None) -> Generator[int, None, None]:
    """
    Returns a list of nodes value from a whole binary tree in Level Order Traverse.
    Level Order traverse: Visit nodes of the tree level-by-level.
    """
    if root is None:
        return

    process_queue = deque([root])

    while process_queue:
        node = process_queue.popleft()
        yield node.data
        if node.left:
            process_queue.append(node.left)
        if node.right:
            process_queue.append(node.right)

# Function to get nodes from left to right at a specific level
def get_nodes_from_left_to_right(root: Node | None, level: int) -> Generator[int, None, None]:
    """
    Returns a list of nodes value from a particular level: Left to right direction of the binary tree.
    """
    def populate_output(root: Node | None, level: int) -> Generator[int, None, None]:
        if not root:
            return
        if level == 1:
            yield root.data
        elif level > 1:
            yield from populate_output(root.left, level - 1)
            yield from populate_output(root.right, level - 1)

    yield from populate_output(root, level)

# Function to get nodes from right to left at a specific level
def get_nodes_from_right_to_left(root: Node | None, level: int) -> Generator[int, None, None]:
    """
    Returns a list of nodes value from a particular level: Right to left direction of the binary tree.
    """
    def populate_output(root: Node | None, level: int) -> Generator[int, None, None]:
        if root is None:
            return
        if level == 1:
            yield root.data
        elif level > 1:
            yield from populate_output(root.right, level - 1)
            yield from populate_output(root.left, level - 1)

    yield from populate_output(root, level)

# Function for zigzag traversal of a binary tree
def zigzag(root: Node | None) -> Generator[int, None, None]:
    """
    ZigZag traverse: Returns a list of nodes value from left to right and right to left, alternatively.
    """
    if root is None:
        return

    flag = 0
    height_tree = height(root)

    for h in range(1, height_tree + 1):
        if not flag:
            yield from get_nodes_from_left_to_right(root, h)
            flag = 1
        else:
            yield from get_nodes_from_right_to_left(root, h)
            flag = 0

# Main function for testing all the functionalities
def main() -> None:
    # Create a binary tree
    root = make_tree()

    # All Traversals of the binary tree
    print(f"In-order Traversal: {list(inorder(root))}")
    print(f"Reverse In-order Traversal: {list(reverse_inorder(root))}")
    print(f"Pre-order Traversal: {list(preorder(root))}")
    print(f"Post-order Traversal: {list(postorder(root))}", "\n")

    # Calculate the height of the tree
    print(f"Height of Tree: {height(root)}", "\n")

    # Complete level-order traversal
    print("Complete Level Order Traversal: ")
    print(f"{list(level_order(root))} \n")

    # Level-wise order traversal
    print("Level-wise order Traversal: ")
    for level in range(1, height(root) + 1):
        print(f"Level {level}:", list(get_nodes_from_left_to_right(root, level=level)))

    # Zigzag order traversal
    print("\nZigZag order Traversal: ")
    print(f"{list(zigzag(root))}")

if __name__ == "__main__":
    import doctest

    doctest.testmod()  # Run doctests
    main() 
