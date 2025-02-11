n = int(input())
brids = list(map(int,input().split()))
shots = int(input())
for i in range(shots):
    x,y = map(int,input().split())
    j = x-1

    if j-1 < 0 and j+1 < len(brids):
        brids[j+1] += (brids[j]-y)
        brids[j] = 0
    elif j-1 < 0 and j+1 >= len(brids):
        brids[j] = 0
    elif j+1 >= len(brids) and j-1>=0:
        brids[j-1] += y-1
        brids[j] = 0
    else:
        brids[j+1] += (brids[j]-y)
        brids[j-1] += (y-1)
        brids[j] = 0

for i in brids:
    print(i)
