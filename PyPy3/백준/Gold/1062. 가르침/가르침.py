### 1062. 가르침 (G4)
### dfs, 백트래킹
import sys
input = sys.stdin.readline
from collections import deque


learned = set(['a', 'n', 't', 'i', 'c'])
learned_field = [False for _ in range(26)]
for next in learned:
    learned_field[ord(next)-97] = True

N, K = map(int, input().split())
words = []
if K < 5:
    print(0)
    exit(0)
for i in range(N):
    tmp = list(input().strip())
    word = set(tmp[4:-4]) - learned
    words.append(word)
        
ans = 0

def dfs(alphabet, count):
    global ans
    if count == K-5: # 배울 수 있는 상한이면
        tmp_ans = count_ans()
        ans = max(ans, tmp_ans)
        return

    if alphabet == 25:
        return
    
    if learned_field[alphabet+1]:
        dfs(alphabet + 1, count)
        return
    
    
    learned_field[alphabet+1] = True
    dfs(alphabet + 1, count + 1) # 다음 알파벳을 선택
    learned_field[alphabet+1] = False
    dfs(alphabet + 1, count) # 다음 알파벳을 선택하지 않음
    
def count_ans():
    tmp_ans = 0
    tmp_learned = set()
    for i in range(26):
        if learned_field[i]:
            tmp_learned.add(chr(i+97))
    for next in words:
        if len(next-tmp_learned) == 0:
            tmp_ans += 1
    
    return tmp_ans 
        
dfs(-1, 0)
print(ans)