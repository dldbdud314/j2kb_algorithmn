'''
< topological sort + BFS advanced >

input: [["math1", "math2"], ["math0", "math2"], ["math2", "math3"], ["math0", "math4"], ["math3", "math5"], ["math4", "math5"]]
output: math0 -> math1 -> math2 -> math4 -> math3 -> math5

1. topological sort
2. bfs(level-by-level)
''' 
from collections import deque

def solution(list):
    if not list:
        return []
    adj_list = topological_advanced(list)
    return bfs_advanced(adj_list)

def bfs_advanced(graph):
    result = []
    sources = find_sources(graph)
    queue = deque([sources])
    while queue:
        cur_level = queue.popleft()
        next_level = []
        for x in cur_level:
            children = graph[x]['dest']
            result.append(x)
            for child in children:
                graph[child]['incoming'] -= 1
                if graph[child]['incoming'] == 0:
                    next_level.append(child)
        if len(next_level) > 0:
            queue.append(next_level)
    return result

def find_sources(tree):
    sources = []
    for key, val in tree.items():
        if val['incoming'] == 0:
            sources.append(key)
    return sources
    
def topological_advanced(list):
    '''
    map = {
        math1 = { 
            incoming : ,
            dest : []
        }, -> inner_map
        ...
    }
    
    '''
    map = {}
    for first, sec in list:
        if first in map:
            map[first]['dest'].append(sec)
        else:
            inner_map = {}
            inner_map['incoming'] = 0
            inner_map['dest'] = [sec]
            map[first] = inner_map #2차원 dictionary 생성
        if sec in map:
            map[sec]['incoming'] += 1
        else:
            inner_map = {}
            inner_map['incoming'] = 1
            inner_map['dest'] = []
            map[sec] = inner_map
    return map

print(solution([["math1", "math2"], ["math0", "math2"], ["math2", "math3"], ["math0", "math4"], ["math3", "math5"], ["math4", "math5"]]))