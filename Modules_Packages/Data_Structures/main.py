from Collection.Trees import Trees, AVLTree

tree = Trees()

tree.Insert(10)
tree.Insert(40)
tree.Insert(60)
tree.Insert(4)
tree.Insert(90)
tree.Insert(32)
tree.Insert(11)
tree.Insert(100)


print(f"Contains 60 : {Trees().Contains(40)}")

tree.PreOrderTraversal()
tree.PostOrderTraversal()
tree.InOrderTraversal()

print(f"Tree Height is {tree.CalculateHeight()}")
print(f"Min Value in a Tree {tree.MinValue()}")
print(f"Max Value in a Tree {tree.CalculateMaxValue()}")


print(*tree.KthDistanceNode(3), ',')
print(f"Leaf Count {tree.CountLeaves()}")
print(f" Count {tree.Size()}")

print(f"Inorder Traversal loops = {tree.IteativeInOrder()}")
print(f"PreOrder Traversal loops = {tree.IterativePreOrder()}")
print(f"PostOrder Traversal loops = {tree.IterativePostOrder1()}")
# print(f"PostOrder Traversal loops = {tree.IterativePostOrder2()}")


print(f"GetAnsistorNodes {tree.GetAnsistors(11)}")


# -------------------------AVL Tree

avltree: AVLTree = AVLTree()

avltree.Insert(4)
avltree.Insert(10)
avltree.Insert(5)
avltree.Insert(20)
avltree.Insert(15)
avltree.Insert(30)
