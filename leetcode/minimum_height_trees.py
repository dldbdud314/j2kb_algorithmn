from collections import deque, defaultdict

class Solution:
    minHeight = float('inf')
    def findMinHeightTrees(self, n, edges):
        def topologicalSort(edge_list):
            #edge case
            if not edge_list:
                return {0 : []}
            #형식: map = {node: []} -> undirectional
            map = defaultdict(list)
            for a, b in edge_list:
                map[a].append(b)
                map[b].append(a)
            return map
        
        def bfs(root, graph):
            height = 0
            queue = deque()
            queue.append([root, height])
            visited = [False] * n
            while queue:
                front = queue.popleft()
                key, height = front[0], front[1]
                if visited[key] == False and graph.get(key):
                    visited[key] = True
                    for x in graph[key]:
                        queue.append([x, height + 1])
            return height - 1
        
        graph = topologicalSort(edges)
        #root 값을 넘기면서 minHeight 갱신
        root_list = []
        for key, _ in graph.items():
            height = bfs(key, graph)
            if height < self.minHeight:
                self.minHeight = height
                root_list.clear()
                root_list.append(key)
            elif height == self.minHeight:
                root_list.append(key)
        return root_list
    
solution = Solution()
print(solution.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))

#time limit exceeded