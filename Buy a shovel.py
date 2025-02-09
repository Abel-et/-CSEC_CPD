price_of_shovel , r = map(int,input().split())
array = []
for i in range(1,10):
    product = price_of_shovel*i
    if product%10 == r or product%10 ==0:
        array.append(i)
print(min(array))
