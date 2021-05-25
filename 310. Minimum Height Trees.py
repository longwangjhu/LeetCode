# https://leetcode.com/problems/minimum-height-trees/

# A tree is an undirected graph in which any two vertices are connected by
# exactly one path. In other words, any connected graph without simple cycles
# is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges
# where edges[i] = [ai, bi] indicates that there is an undirected edge between
# the two nodes ai and bi in the tree, you can choose any node of the tree as
# the root. When you select a node x as the root, the result tree has height h.
# Among all possible rooted trees, those with minimum height (i.e. min(h))  are
# called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any
# order.

# The height of a rooted tree is the number of edges on the longest downward
# path between the root and a leaf.

###############################################################################

# topological sort -> stop when remaining nodes <= 2

from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2: return list(range(n))
        
        graph = defaultdict(set)
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)
        
        # init
        queue = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                queue.append(i)
        
        n_remain = n
        while n_remain > 2:
            curr_len = len(queue)
            n_remain -= curr_len
            for _ in range(curr_len):
                node = queue.popleft()
                # remove the edge left--neigh
                neigh = graph[node].pop()
                graph[neigh].remove(node)
                
                if len(graph[neigh]) == 1:
                    queue.append(neigh)
        return queue