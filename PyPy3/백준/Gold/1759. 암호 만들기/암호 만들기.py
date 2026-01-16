### 1759. 암호 만들기
### dfs, 백트래킹
import sys
input = sys.stdin.readline

L, N = map(int, input().split())
l = list(map(str, input().split()))
l.sort()
ans = []

def check_ans(mo, ja):
    if mo == True and ja >= 2:
        return True
    return False

def dfs(mo, ja, idx, res):
    if idx == N:
        if check_ans(mo, ja) and len(res) == L:
            return res
        return

    if l[idx] in ['a', 'e', 'i', 'o', 'u']:
        tmp1 = dfs(True, ja, idx + 1, res + l[idx])
        tmp2 = dfs(mo, ja, idx + 1, res)
        if tmp1: ans.append(tmp1)
        if tmp2: ans.append(tmp2)


    else:
        tmp3 = dfs(mo, ja + 1, idx + 1, res + l[idx])
        tmp4 = dfs(mo, ja, idx + 1, res)
        if tmp3: ans.append(tmp3)
        if tmp4: ans.append(tmp4)


dfs(False, 0, 0, "")
for a in ans:
    print(a)

