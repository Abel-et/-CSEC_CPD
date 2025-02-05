game = int(input())
count = 0
a,b = [],[]
for i in range(game):
    x, y = map(int, input().split())
    a.append(x);b.append(y)
for i in a:
    if i in b:
        c=b.count(i)
        count+=c
    else:
        continue
print(count)
