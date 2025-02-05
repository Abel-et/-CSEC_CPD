num_magnet= int(input())
group= 0
s, identifier = "",""
for i in range(num_magnet):
    s = input()
    if identifier =="":
        identifier = s
        group+=1
    elif identifier != s:
        identifier = s
        group += 1
    else:
        continue
print(group)
