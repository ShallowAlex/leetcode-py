"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        from collections import deque
        if not node:
            return node
        
        visited = {}
        visited[node] = Node(node.val, [])
        queue = deque([node])

        while queue:
            p = queue.popleft()
            for n in p.neighbors:
                if n not in visited:
                    visited[n] = new_n = Node(n.val, [])
                    queue.append(n)
                visited[p].neighbors.append(visited[n])
        return visited[node]