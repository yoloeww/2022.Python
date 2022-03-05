import collections 

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # 初始化队列同时将第一层节点加入队列中，即根节点
        Q = collections.deque([root])
        
        # 外层的 while 循环迭代的是层数
        while Q:
            
            # 记录当前队列大小
            size = len(Q)
            
            # 遍历这一层的所有节点
            for i in range(size):
                
                # 从队首取出元素
                node = Q.popleft()
                
                # 连接
                if i < size - 1:
                    node.next = Q[0]
                
                # 拓展下一层节点
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        # 返回根节点
     

