num_card = int(input())
cards = list(map(int,input().split()))
sereja , dima =0,0
i ,j = 0,num_card-1
for r in range(num_card):
    if r%2==0:
        if cards[i]>=cards[j]:
            sereja+=cards[i]
            i+=1
        else:
            sereja += cards[j]
            j-=1
    else:
        if cards[i]>= cards[j]:
            dima += cards[i]
            i+=1
        else:
            dima += cards[j]
            j -=1
print(sereja,dima)
