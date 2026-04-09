n = int(input())
count=0
a = list(map(int, input().split()))
for i in range(n):
    if a[i]>0:
        count+=1
print(count)