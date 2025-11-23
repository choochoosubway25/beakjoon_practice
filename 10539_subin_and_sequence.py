sequence_num = int(input())
sequence_b = list(map(int, input().split()))

'''
let sequence a as a_1, a_2, ..., a_n
and sequence b as b_1, b_2, ..., b_n
then sum of a_1 to a_n is n*b_n
and sum of a_1 to a_(n-1) is (n-1)*b_(n-1) (especially where n>=2)
so a_n = n*b_n - (n-1)*b_(n-1)
but sequence a and b are start with index 0
therefore we modify sequences' indices as n -> n-1
it makes a_(n-1) = n*b_(n-1) - (n-1)*b_(n-2) or
a_n = (n+1)*b_n - b*b_(n-1)
'''
result = str(sequence_b[0])
for i in range(1, sequence_num):
    result += f' {(i+1)*sequence_b[i] - i*sequence_b[i-1]}'
print(result)
