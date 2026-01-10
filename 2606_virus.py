import sys

vertex_count = int(sys.stdin.readline())
edge_count = int(sys.stdin.readline())
edge_dict = dict()
for _ in range(vertex_count):
    edge_dict[_ + 1] = list()
for i in range(edge_count):
    vertex_1, vertex_2 = map(int, sys.stdin.readline().split())
    edge_dict[vertex_1].append(vertex_2)
    edge_dict[vertex_2].append(vertex_1)
infected = [1]
inspection = [1]
while len(inspection) > 0:
    inspector = inspection.pop(0)
    connections = edge_dict[inspector]
    for num in connections:
        if num not in infected:
            infected.append(num)
            inspection.append(num)
print(len(infected) - 1)
