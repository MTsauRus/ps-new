### 2817. 부분 수열의 합
### 완전 탐색, dfs, S2?

T = int(input())

def dfs(idx, use, res):
    global ans
    
    if res > K:
        return
    
    if idx == N:
        return
    
    if use:
        res += nums[idx]
        if res == K:
            ans += 1
    
    dfs(idx+1, True, res)
    dfs(idx+1, False, res)

for t in range(1, T+1):
    N, K = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    ans = 0
    dfs(0, True, 0)
    dfs(0, False, 0)
    print(f'#{t} {ans}')