xx = []
yy = []

for i in range(3):
    x, y = map(int, input().split())
    xx.append(x)
    yy.append(y)
xx.sort()
yy.sort()
    
ans = []
if xx[0] == xx[1]:
    ans.append(xx[2])
else:
    ans.append(xx[0])

if yy[0] == yy[1]:
    ans.append(yy[2])
else:
    ans.append(yy[0])

print(*ans)