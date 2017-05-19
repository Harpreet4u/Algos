# https://www.hackerrank.com/challenges/crush

# Overlapping interval problem
N, M = map(int, raw_input().strip().split())

ls = []
while M:
    M-=1
    a, b, k = map(int, raw_input().strip().split())
    ls.append((a, (-1, k)))
    ls.append((b, (1, k)))

ls.sort() # nlogn
maxx = 0
cnt = 0
for i, (j, k) in ls:
    cnt += k if j==-1 else -k
    maxx = max(maxx, cnt)
    
print maxx
