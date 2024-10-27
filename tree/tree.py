#         二叉树
#          [1]
#         /  \
#      [2]   [3]
#     /  \   / \
#   [4] [5][6] [7]
#   / \
# [8] [9]


# 节点类
class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value  # 存储数据
        self.left = left  # 左子树
        self.right = right  # 右子树


# 树类
class Tree:
    # 初始化根节点
    def __init__(self, root=None):
        self.root = root  # 初始化根节点
        self.ls = []  # 存储节点地址
        self.pre_nodes = []  # 先序遍历存储
        self.in_nodes = []  # 中序遍历存储
        self.post_nodes = []  # 后序遍历存储

    # 添加节点
    def insert_node(self, value):
        # 实例化树节点
        node = TreeNode(value)
        # 若根节点为空，添加为根节点，并存储其地址
        if self.root is None:
            self.root = node
            self.ls.append(self.root)
        else:
            # 以第一个节点为根节点
            root_node = self.ls[0]
            # 左子树为空，添加为左子节点，并存储其地址
            if root_node.left is None:
                root_node.left = node
                self.ls.append(root_node.left)
            # 右子树为空，添加为右子节点，并存储其地址
            elif root_node.right is None:
                root_node.right = node
                self.ls.append(root_node.right)
                # 删除存储的第一个节点，因其左右子节点均为非空
                self.ls.pop(0)

    # 前序遍历preorder
    """
    根节点 -> 左子树 -> 右子树
    [1,2,4,8,9,5,3,6,7]
    """
    def preorder(self, root):
        # 节点判空
        if root is None:
            return
        # 遍历根节点
        self.pre_nodes.append(root.value)
        # 遍历左子树
        self.preorder(root.left)
        # 遍历右子树
        self.preorder(root.right)

    def preorder_stack(self, root):
        if root is None:
            return
        stack = []
        result = []
        node = root
        while node or stack: # node 或 stack 非空时进行循环
            while node: # 查找当前节点的左子节点，存入 stack 中
                result.append(node.value) # result 存储当前节点值
                stack.append(node)
                node = node.left
            node = stack.pop() # 当前节点不存在左子节点时，退出循环，且将其移出 stack 并获取其值
            node = node.right # 查找当前节点的右子节点
        print(result)

    # 中序遍历inorder
    '''
    左子树 -> 根节点 -> 右子树
    [8,4,9,2,5,1,6,3,7]
    '''
    def inorder(self, root):
        # 节点判空
        if root is None:
            return
        # 遍历左子树
        self.inorder(root.left)
        # 遍历根节点
        self.in_nodes.append(root.val)
        # 遍历右子树
        self.inorder(root.right)

    def inorder_stack(self, root):
        if root is None:
            return
        stack = []
        result = []
        node = root
        while node or stack: # node 或 stack 非空时进行循环
            while node: # 查找当前节点的左子节点，存入 stack 中
                stack.append(node)
                node = node.left
            node = stack.pop() # 当前节点不存在左子节点时，退出循环，且将其移出 stack 并获取其值
            result.append(node.value) # result 存储当前节点值
            node = node.right  # 查找当前节点的右子节点
        print(result)

    # 后序遍历postorder
    '''
    左子树 -> 右子树 -> 根节点
    [8,9,4,5,2,6,7,3,1]
    '''
    def postorder(self, root):
        # 节点判空
        if root is None:
            return
        # 遍历左子树
        self.postorder(root.left)
        # 遍历右子树
        self.postorder(root.right)
        # 遍历根节点
        self.post_nodes.append(root.val)

    def postorder_stack(self, root):
        if root is None:
            return
        stack = []
        seq = []
        result = []
        node = root
        while node or stack: # node 或 stack 非空时进行循环
            while node: # 查找当前节点的右子节点，存入 stack 中
                seq.append(node.value) # seq 存储当前节点值
                stack.append(node)
                node = node.right
            node = stack.pop() # 当前节点不存在右子节点时，退出循环，且将其移出 stack 并获取其值
            node = node.left  # 查找当前节点的左子节点
        while seq:
            result.append(node.value) # 将 seq 中的元素逆序添加到 result 中
        print(result)

    # 层次遍历levelorder
    '''
    [1,2,3,4,5,6,7,8,9]
    '''
    def levelorder_stack(self, root):
        if root is None:
            return
        queue = []
        result = []
        node = root
        queue.append(node) # 根节点入队
        while queue: # 队列非空时进行循环
            node = queue.pop(0)  # 当前节点不存在左子节点时，退出循环，且将其移出 stack 并获取其值
            result.append(node.value)  # result 存储当前节点值
            if node.left is not None: # 左子节点非空，入队
                queue.append(node.left)
            if node.right is not None: # 右子节点非空，入队
                queue.append(node.right)
        print(result)

    # 查找叶子节点
    def findleafnode(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            print(root.value)
        self.findleafnode(root.left)
        self.findleafnode(root.right)

    # 树高度
    def height(self, root):
        if root is None:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        if lh > rh:
            return lh + 1
        else:
            return rh + 1


if __name__ == '__main__':
    tr = Tree()
    for i in range(1, 10):
        tr.insert_node(i)
    tr.preorder(tr.root)
    pre_nodes = tr.pre_nodes
    print(pre_nodes)
    print(tr.height(tr.root))
