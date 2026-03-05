import sys

'''
number of segment for each digit
0 : 6
1 : 2
2 : 5
3 : 5
4 : 4
5 : 5
6 : 6
7 : 3
8 : 7
9 : 6
digits for each segment number:
2 : 1
3 : 7
4 : 4
5 : 2, 3, 5
6 : 0, 6, 9
7 : 8
'''
segment_dict = {
    8: "11:11", 9: "11:17", 10: "11:14", 11: "11:15",
    12: "11:16", 13: "11:18", 14: "10:41", 15: "10:47",
    16: "10:44", 17: "10:45", 18: "10:46", 19: "10:48",
    20: "09:16", 21: "08:01", 22: "08:07", 23: "08:04",
    24:"08:05", 25:"08:00", 26:"08:08"
}
segment_count = int(sys.stdin.readline())
if segment_count in segment_dict.keys():
    print(segment_dict[segment_count])
else:
    print('Impossible')
