a = int(input())
n = 0
i = 1
while i * i <= a:
    if a % i == 0:
        if i * i == a:
            n += 1
        else:
            n += 2
    i += 1

print(n)