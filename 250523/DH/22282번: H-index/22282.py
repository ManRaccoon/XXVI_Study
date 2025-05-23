import sys
input = sys.stdin.readline

n = int(input())
papers = []
for _ in range(n):
    paper = int(input())
    papers.append(paper)
papers.sort(reverse=True)
result = 0
for i in range(n):
    if papers[i] >= i + 1:
        result += 1
    else:
        break
print(result)
