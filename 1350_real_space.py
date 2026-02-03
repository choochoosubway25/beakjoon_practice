import sys

file_count = int(sys.stdin.readline())
file_sizes = list(map(int, sys.stdin.readline().split()))
cluster_size = int(sys.stdin.readline())
usage_size = 0
for i in range(file_count):
    usage_size += (file_sizes[i] // cluster_size) * cluster_size
    usage_size += (file_sizes[i] % cluster_size != 0) * cluster_size
print(usage_size)
