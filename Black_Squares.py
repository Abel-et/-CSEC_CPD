calories = list(map(int,input().split()))
s = input()
wasted_calories = 0
for i in range(len(s)):
    p = int(s[i])
    wasted_calories +=calories[p-1]
print(wasted_calories)
