friend,height = map(int ,input().split())
    friends_height = list(map(int,input().split()))
    width = 0
    for i in friends_height:
        if height < i :
            width += 2
        else:
            width += 1
    print(width)
