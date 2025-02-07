s = input()
current = ord('a')
move = 0
for i in s:
    target = ord(i)
    clockwise = (target - current)%26
    counter = (current - target)%26
    move += min(clockwise,counter)
    current = target
print(move)

