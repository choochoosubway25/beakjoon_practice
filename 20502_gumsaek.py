import sys
import heapq

# 기본 세팅
article_count, keyword_count = map(int, sys.stdin.readline().split())
ranks = list(map(int, sys.stdin.readline().split()))
# 각 게시글의 키워드 저장
article_keyword_dict = dict()
for i in range(article_count):
    inputs = sys.stdin.readline().split()
    article_keyword_dict[i] = (int(inputs[0]), set(inputs[1:]))
# 질의 응답 준비
question_count = int(sys.stdin.readline())
for _ in range(question_count):
    question_keyword = sys.stdin.readline().strip()
    answer_articles = list()
    heapq.heapify(answer_articles)
    for i in range(article_count):
        if question_keyword in article_keyword_dict[i][1]:
            heapq.heappush(answer_articles, (ranks[i], i))
    result = []
    for j in range(len(answer_articles)):
        article = heapq.heappop(answer_articles)[1]
        result.append(article + 1)
    if len(result) > 0:
        print(' '.join(map(str, result)))
    else:
        print(-1)
