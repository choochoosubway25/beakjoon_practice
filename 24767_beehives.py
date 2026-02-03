import sys

while True:
    inputs = sys.stdin.readline().strip()
    if inputs == "0.0 0":
        break
    input_list = inputs.split()
    distant = float(input_list[0])
    hive_count = int(input_list[1])
    hive_positions = [(0.0, 0.0) for _ in range(hive_count)]
    indices_set = set([c for c in range(hive_count)])
    sour_set = set()
    for k in range(hive_count):
        x, y = map(float, sys.stdin.readline().split())
        hive_positions[k] = (x, y)
    while len(indices_set) > 0:
        i0 = indices_set.pop()
        inspect_list = [i0]
        sour_count = 0
        while len(inspect_list) > 0:
            i = inspect_list.pop()
            xi, yi = hive_positions[i]
            for j in indices_set:
                xj, yj = hive_positions[j]
                if (xi - xj) ** 2 + (yi - yj) ** 2 <= distant ** 2:
                    inspect_list.append(j)
                    if sour_count == 0:
                        sour_set.add(i)
                        sour_count += 1
                    sour_set.add(j)
                    sour_count += 1
            indices_set = indices_set - sour_set
    sour_total = len(sour_set)
    print(f"{sour_total} sour, {hive_count - sour_total} sweet")
