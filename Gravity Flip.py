column = int(input())
toy_cube = list(map(int,input().split()))
toy_cube.sort()
for i in toy_cube:
    print(i,end=" ")
