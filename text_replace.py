import sys

input = sys.stdin.readlines()

# 마지막 행은 0이 두 개이다.
while True:
    A, B = map(int, input.split())

    if A == 0 and B == 0:
	    break
    else:
		textline = A + B
	    print(A + B)
textline.replace('$$', '$')
textline.replace('\\', '$<br>')
textline.replace('\begin{aligned}', '')
textline.replace('\end{aligned}', '')
textline.replace('&', '')
textlist = map(str, textline.strip())
for line in textlist:
	print(line)

