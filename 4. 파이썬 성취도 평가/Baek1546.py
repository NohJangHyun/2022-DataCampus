N = int(input())
num=list(map(int,input().split()))
M = max(num)
S = 0.0
for i in range(N):
    S += num[i]/M*100
print(S/N)