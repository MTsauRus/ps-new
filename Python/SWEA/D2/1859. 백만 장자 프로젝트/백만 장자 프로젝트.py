T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    a = int(input())
    l = list(map(int, input().split()))
    ans = 0
    now_max = l[-1]
    for i in range(a-2, -1, -1):
        now = l[i]
        if now >= now_max:
            now_max = now
            continue
        ans += now_max-now
    print(f"#{test_case} {ans}")
             
    # ///////////////////////////////////////////////////////////////////////////////////
