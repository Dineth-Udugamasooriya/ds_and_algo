class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursively(self.root, key)

    def _insert_recursively(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_recursively(root.left, key)
        else:
            root.right = self._insert_recursively(root.right, key)
        return root

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_recursively(root.left, key)
        return self._search_recursively(root.right, key)

    def inorder_traversal(self):
        return self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, root):
        if root is None:
            return []
        return (
            self._inorder_traversal_recursive(root.left)
            + [root.key]
            + self._inorder_traversal_recursive(root.right)
        )

    def remove(self, key):
        self.root = self._remove_recursively(self.root, key)

    def _remove_recursively(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._remove_recursively(root.left, key)
        elif key > root.key:
            root.right = self._remove_recursively(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children, find the inorder successor
            root.key = self._get_min_value(root.right)
            root.right = self._remove_recursively(root.right, root.key)

        return root

    def _get_min_value(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.key

# Example usage:
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder Traversal:", bst.inorder_traversal())

key_to_remove = 30
bst.remove(key_to_remove)
print(f"Removed {key_to_remove} from the BST.")
print("Inorder Traversal after removal:", bst.inorder_traversal())
