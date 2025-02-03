nums = int(input())
winner = input()
anton = winner.count("A")
danik = winner.count("D")
if anton>danik:
  print("Anton")
elif anton<danik:
  print("Danik")
else:
  print("Friendship")
