'''
score_dict1 = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
score_dict2 = {'+': 0.3, '0': 0.0, '-': -0.3}
score = str(input())
result = 0.0
result += score_dict1[score[0]]
if score[0] != 'F':
	result += score_dict2[score[1]]
print('{0:0.1f}'.format(result))
'''
'''
word = str(input())
alphabets = [-1 for i in range(26)]
length = len(word)
for i in range(length):
	idx = ord(word[i]) - 97
	if alphabets[idx] < 0:
		alphabets[idx] = i
result = ''
for indeces in alphabets:
	result += str(indeces)
	result += ' '
print(result[:-1])
'''


def sublist_max(profits, start, end):
	# 여기에 코드를 작성하세요
	if start == end:
		return profits[start]
	mid = (start + end) // 2
	profit1 = sublist_max(profits, start, mid)
	profit2 = sublist_max(profits, mid + 1, end)
	profit3 = max_crossing_sum(profits, start, end)
	return max(profit1, profit2, profit3)


def max_crossing_sum(profits, start, end):
	mid = (start + end) // 2
	left_sum = 0
	left_max = profits[mid]
	for i in range(mid, start - 1, -1):
		left_sum += profits[i]
		left_max = max(left_max, left_sum)
	right_sum = 0
	right_max = profits[mid + 1]
	for j in range(mid + 1, end + 1):
		right_sum += profits[j]
		right_max = max(right_max, right_sum)
	return left_max + right_max


# 테스트 코드
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))
