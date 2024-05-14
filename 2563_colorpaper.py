# 색종이는 가로, 세로 크기 100인 정사각형
areas = 0
whitepaper = [[0 for j in range(100)] for i in range(100)]

paper_num = int(input())
# 검은 색종이를 크기 1의 작은 색종이로 간주하여 가로, 세로 10칸씩 이어 붙인다.
for _ in range(paper_num):
    x, y = map(int, input().split())
    for n in range(10):
        for m in range(10):
            # 색종이의 위치가 0보다 큰 자연수로 주어지므로 python의 indexing 대응을 위해 각 위치에서 1을 빼준다.
            # 또한 색종이가 2개 이상 붙어도 넓이는 1로 취급하므로 if 구문을 쓸 필요 없이 색종이에 포함되는 위치의 값을 1로 고정한다.
            whitepaper[x+n-1][y+m-1] = 1

for k in range(100):
    #각 줄에 색종이가 붙은 수를 합하여 더해준다.
    areas += sum(whitepaper[k])

print(areas)