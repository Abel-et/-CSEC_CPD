horseshose= list(map(int,input().split()))
new_shose = set(horseshose)
new = 0
for i in new_shose:
    new += horseshose.count(i)
print(new-len(new_shose))
