contest = int(input())
sure=0
for i in range(contest):
    petya,vasya,tonay = map(int,input().split())
    sum = petya +vasya+ tonay
    if sum> 1:
        sure+=1
print(sure)
