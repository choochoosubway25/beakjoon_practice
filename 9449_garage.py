import sys
import math


sandlot_width, sandlot_height, garage_width, garage_height = map(int, sys.stdin.readline().split())
multiple_width = sandlot_width / garage_width
multiple_height = sandlot_height / garage_height
optimal_width = math.floor((multiple_width - 1) / 2) + 1
optimal_height = math.floor((multiple_height - 1) / 2) + 1
print(optimal_width * optimal_height)