s = list(input())
t = list(input())
liss_move = 0
i=0
for instraction in t:
    if s[liss_move] == instraction:
        liss_move +=1
        if liss_move >len(s):
            break
print(liss_move+1)
