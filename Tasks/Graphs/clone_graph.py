class UndirectedGraphNode:
	def __init__(self, x):
	self.label = x
	self.neighbors = []

class Solution:
	def cloneGraph(self, node):
        from collections import deque
        q = deque()
        h = {}
        q.append(node)
        cnode = UndirectedGraphNode(node.label)
        h[node] = cnode
        while(len(q) > 0):
            t = q[0]
            q.popleft()
            for i in t.neighbors:
                if i not in h:
                    copy = UndirectedGraphNode(i.label)
                    h[i] = copy
                    q.append(i)
                h[t].neighbors.append(h[i])
                    
        return cnode


			new = TreeNode(
	
		
		

