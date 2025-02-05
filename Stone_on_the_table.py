size = int(input())
stone = input()
count = 0
if len(stone) < 2:
    print(0)
else:
    for i in range(len(stone) - 1):
        if stone[i] == stone[i + 1]:
            count += 1
    print(count)
