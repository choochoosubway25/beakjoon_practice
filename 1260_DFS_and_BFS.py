import sys
from collections import deque

vertices_num, edges_num, start_vertex = map(int, sys.stdin.readline().split())
graphs = dict()
for i in range(vertices_num):
    graphs[i+1] = list()
for j in range(edges_num):
    v, u = map(int, sys.stdin.readline().split())
    graphs[v].append(u)
    graphs[u].append(v)
dfs_queue = deque()
dfs_visit_list = list()
bfs_queue = deque()
bfs_visit_list = list()
dfs_queue.append(start_vertex)
bfs_queue.append(start_vertex)
visited = set()
while len(dfs_queue) > 0:
    vertex = dfs_queue.popleft()
    if vertex not in visited:
        visited.add(vertex)
        dfs_visit_list.append(vertex)
        neighbors = graphs[vertex]
        neighbors.sort(reverse=True)
        for neighbor in neighbors:
            dfs_queue.appendleft(neighbor)
visited = set()
while len(bfs_queue) > 0:
    vertex = bfs_queue.popleft()
    if vertex not in visited:
        visited.add(vertex)
        bfs_visit_list.append(vertex)
        neighbors = graphs[vertex]
        neighbors.sort()
        for neighbor in graphs[vertex]:
            if neighbor not in visited:
                bfs_queue.append(neighbor)
print(' '.join(map(str, dfs_visit_list)))
print(' '.join(map(str, bfs_visit_list)))
