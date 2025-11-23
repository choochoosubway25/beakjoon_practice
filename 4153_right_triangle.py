while True:
    inputs = str(input())
    if inputs == '0 0 0':
        break
    result = "wrong"
    edges = list(map(int, inputs.split()))
    edges.sort()
    if edges[0]**2 + edges[1]**2 == edges[2]**2:
        result = 'right'
    print(result)
