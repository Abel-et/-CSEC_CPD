limka , bear = map(int, input().split())
count = 0
while True:
    if limka > bear:
        break
    limka = limka*3
    bear = bear*2
    count +=1
print(count)
