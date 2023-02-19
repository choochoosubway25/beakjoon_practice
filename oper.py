def oper(a: int, b:int) -> int:
    result = (a+b)*(a-b)
    return result


A, B = map(int, input().split())
print(oper(A, B))