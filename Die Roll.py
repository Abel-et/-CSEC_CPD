y , w = map(int, input().split())
p = max(y,w)
prob = 6 - p +1
dinominator =6
nominator = prob
common = gcd(dinominator,nominator)
nominator //= common
dinominator //= common
print(f'{nominator}/{dinominator}')
