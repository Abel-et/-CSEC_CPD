limka , bob = map(int,input().split())
count = 0
while bob>=limka:
    limka+= limka*3
    bob+=bob*2
    count +=1
print(count)
