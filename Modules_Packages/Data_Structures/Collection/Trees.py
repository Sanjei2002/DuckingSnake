from typing import Optional
from typing import List


class AVLTree:

    def __init__(self):
        self.__root = None

    def Insert(self, value):
        self.__root = self.__Insert(self.__root, value=value)

    def __Insert(self, node: "AVLNode", value) -> "AVLNode":

        if not node:
            return AVLNode(value)

        if value < node.Value:
            node.Left = self.__Insert(node=node.Left, value=value)
        elif value > node.Value:
            node.Right = self.__Insert(node=node.Right, value=value)

        node.Height = self.Height(node)

        balanceFactor = self.BalanceFactor(node=node)

        if balanceFactor > 1:  # Left Heavy
            balanceFactor = self.BalanceFactor(node=node.Left)
            if balanceFactor < 0:  # Right node of left tree causes imbalance so Rl
                return self.LeftRightRotation(node)
            else:  # LL
                return self.RightRotation(node)
        elif balanceFactor < -1:  # right heavy

            balanceFactor = self.BalanceFactor(node=node.Right)
            if balanceFactor > 0:  # Left node of Right tree causes imbalance so LR
                return self.RightLeftRotation(node)
            else:  # RR
                return self.LeftRotation(node)

        return node

    def LeftRotation(self, rootnode: "AVLNode") -> "AVLNode":

        if not rootnode:
            return rootnode
        newroot = rootnode.Right
        rootnode.Right = newroot.Left
        newroot.Left = rootnode
        # Update heights
        rootnode.Height = self.Height(rootnode)
        newroot.Height = self.Height(newroot)

        return newroot

    def RightRotation(self, rootnode: "AVLNode") -> "AVLNode":
        if not rootnode:
            return rootnode
        newroot = rootnode.Left
        rootnode.Left = newroot.Right
        newroot.Right = rootnode
        # Update heights
        rootnode.Height = self.Height(rootnode)
        newroot.Height = self.Height(newroot)

        return newroot

    def LeftRightRotation(self, rootnode: "AVLNode") -> "AVLNode":
        if not rootnode:
            return
        rootnode.Right = self.LeftRotation(rootnode.Right)
        return self.LeftRotation(rootnode)

    def RightLeftRotation(self, rootnode: "AVLNode") -> "AVLNode":
        if not rootnode:
            return
        rootnode.Left = self.RightRotation(rootnode=rootnode.Left)
        return self.LeftRotation(rootnode)

    def BalanceFactor(self, node: "AVLNode") -> int:

        return self.Height(node=node.Left) - self.Height(node=node.Right)

    def Height(self, node: "AVLNode") -> int:
        if not node:
            return -1
        return node.Height

    def CalculateHeight(self, node: "AVLNode") -> int:

        if not node:
            return 0

        return (max(self.CalculateHeight(node=node.Left), self.CalculateHeight(node=node.Right)) + 1)


class AVLNode:

    @property
    def Value(self):
        return self.__value

    @Value.setter
    def Value(self, value):
        self.__value = value

    @property
    def Left(self) -> "AVLNode":
        return self.__left

    @Left.setter
    def Left(self, value: "AVLNode"):
        self.__left = value

    @property
    def Right(self) -> "AVLNode":
        return self.__right

    @Right.setter
    def Right(self, value: "AVLNode"):
        self.__right = value

    @property
    def Height(self) -> int:
        return self.__height

    @Height.setter
    def Height(self, value: int):
        self.__height = value

    def __init__(self, value):
        self.__left = None
        self.__right = None
        self.__value = value
        self.__height = 0


class Trees:

    def __init__(self):
        self.root = None

    def Insert(self, item) -> None:
        new_node = Node(item)
        current: Node = self.root

        # Handling First element handling
        if not current:
            self.root = new_node
            return

        while current != None:
            if new_node.Value < current.Value:
                if current.Left:
                    current = current.Left
                else:
                    current.Left = new_node
                    break
            elif new_node.Value > current.Value:
                if current.Right:
                    current = current.Right
                else:
                    current.Right = new_node
                    break

    def Contains(self, item) -> bool:

        current: Node = self.root

        # Handling First element handling
        if not current:
            return False

        while current != None:
            if item < current.Value:
                current = current.Left

            elif item > current.Value:
                current = current.Right

            elif item == current.Value:
                return True
        else:
            return False

    def PreOrderTraversal(self) -> None:
        print("===Root Left Right ")
        # recurssion
        self.__RootLeftRight(self.root)

    def PostOrderTraversal(self) -> None:
        print("===Left Right Root")
        # recurssion
        self.__LeftRightRoot(self.root)

    def InOrderTraversal(self) -> None:
        print("===Left Root Right")
        # recurssion
        self.__LeftRootRight(self.root)

    def CalculateHeight(self) -> int:
        return self.__CalculateHeightRec(self.root)

    def MinValue(self) -> int:
        return self.__CalculateMInValue(self.root)

    def KthDistanceNode(self, distance: int) -> list:
        self.__outPutList = list()
        self.__KthDistanceNode(self.root, 0, distance)
        return self.__outPutList

    def GetAnsistors(self, value: int) -> List[int]:
        self.__Ansistors = list()
        self.__GetAnsistors(node=self.root, child=value)
        return self.__Ansistors

    def __GetAnsistors(self, node: "Node", child: int) -> bool:
        if not node:
            return False

        if node.Value == child:
            return True

        if self.__GetAnsistors(node=node.Left, child=child) or self.__GetAnsistors(node=node.Right, child=child):
            self.__Ansistors.append(node.Value)
            return True

        return False

    def IterativePreOrder(self) -> list["Node"]:
        items: list[Node] = list()
        stack: list[Node] = list()
        stack.append(self.root)

        while stack:
            # process node
            curr = stack.pop()
            items.append(curr.Value)

            if curr.Right:
                stack.append(curr.Right)
            if curr.Left:
                stack.append(curr.Left)

        return items

    def IterativePostOrder1(self) -> list["Node"]:

        stack: list[Node] = list()
        stack2: List[Node] = list()
        stack.append(self.root)

        while stack:
            # process node
            curr = stack.pop()
            stack2.append(curr)

            if curr.Left:
                stack.append(curr.Left)
            if curr.Right:
                stack.append(curr.Right)

        stack2.reverse()
        return [item.Value for item in stack2]

    def IterativePostOrder2(self) -> list["Node"]:
        item: list[Node] = list()
        stack: list[Node] = list()
        lastProcessed: Node
        curr = self.root

        while curr or stack:
            # process node
            while curr:
                stack.append(curr)
                curr = curr.Left

            curr = stack[-1]  # peak

            if curr.Right and curr.Right != lastProcessed:
                curr = curr.Right
            else:
                curr = stack.pop()
                item.append(curr.Value)
                lastProcessed = curr

        return item

    def IteativeInOrder(self) -> list:

        items = list()
        stack = list()
        curr = self.root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.Left

            # at this point curr is null
            curr = stack.pop()
            items.append(curr.Value)

            curr = curr.Right

        return items

    def CountLeaves(self):
        return self.__CountLeaves(self.root)

    def Size(self) -> int:
        return self.__Size(self.root)

    def CalculateMaxValue(self):
        return self.__CalculateMaxVaule(self.root)

    def __CalculateMaxVaule(self, node="Node") -> int:
        if not node:
            return float('-inf')

        leftMax = self.__CalculateMaxVaule(node=node.Left)
        rightMAx = self.__CalculateMaxVaule(node=node.Right)

        return max(leftMax, rightMAx, node.Value)

    def __Size(self, node="Node") -> int:
        if not node:
            return 0

        return 1 + self.__Size(node=node.Left) + self.__Size(node=node.Right)

    def __CountLeaves(self, node="Node") -> int:
        if not node:
            return 0

        if not node.Left and not node.Right:
            return 1

        leftTreeChidCount = self.__CountLeaves(node=node.Left)
        rightTreeChildCount = self.__CountLeaves(node=node.Right)

        return leftTreeChidCount + rightTreeChildCount

    def __KthDistanceNode(self, node: "Node", currDistance, ExpectedDistance):
        if not node or (currDistance > ExpectedDistance):
            return

        if currDistance == ExpectedDistance:
            self.__outPutList.append(node.Value)
            return

        self.__KthDistanceNode(
            node=node.Left, currDistance=currDistance+1, ExpectedDistance=ExpectedDistance)
        self.__KthDistanceNode(
            node=node.Right, currDistance=currDistance+1, ExpectedDistance=ExpectedDistance)

    def __CalculateMInValue(self, node: "Node") -> int:

        if not node:
            return float('inf')

        leftMin = self.__CalculateMInValue(node.Left)
        rightMin = self.__CalculateMInValue(node=node.Right)

        return min(leftMin, rightMin, node.Value)

        if not firstTree:
            if not secondTree:
                return True
            else:
                return False

        isLeftTreeEqual = self.TraverseTwoTree(firstTree.left, secondTree.left)
        if not isLeftTreeEqual:
            return False

        # processing Node
        isRootVauleEqual = firstTree.val == secondTree.val
        if not isRootVauleEqual:
            return False

        isRightTreeEqual = self.TraverseTwoTree(
            firstTree.right, secondTree.right)
        if not isRightTreeEqual:
            return False

        return True

    def __CalculateHeightRec(self, node: "Node") -> int:
        if not node:
            return 0

        return 1 + max(self.__CalculateHeightRec(node=node.Left), self.__CalculateHeightRec(node=node.Right))

    def __ProcessNode(self, node: "Node") -> None:
        print(f"{node.Value},")

    def __LeftRightRoot(self, node: "Node") -> None:

        if not node:
            return
        # left
        self.__LeftRightRoot(node.Left)
        # right
        self.__LeftRightRoot(node=node.Right)
        # root
        self.__ProcessNode(node=node)

    def __RootLeftRight(self, node: "Node") -> None:

        if (node == None):
            return
        # Root
        self.__ProcessNode(node)
        # left
        self.__RootLeftRight(node=node.Left)
        # right
        self.__RootLeftRight(node=node.Right)

    def __LeftRootRight(self, node: "Node") -> None:

        if not node:
            return

        # left
        self.__LeftRootRight(node=node.Left)
        # root
        self.__ProcessNode(node=node)
        # right
        self.__LeftRootRight(node=node.Right)


class Node:

    @property
    def Value(self):
        return self.__value

    @Value.setter
    def Value(self, value):
        self.__value = value

    @property
    def Left(self):
        return self.__left

    @Left.setter
    def Left(self, node):
        self.__left = node

    @property
    def Right(self):
        return self.__right

    @Right.setter
    def Right(self, node):
        self.__right = node

    def __init__(self, value):
        self.__left = None
        self.__right = None
        self.__value = value
