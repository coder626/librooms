import random


totalOdd = 0
total = 0

result = 0

for i in range (10000000):
  a = random.randint(0,9)
  b = random.randint(0,9)
  c = random.randint(0,9)
  d = random.randint(0,9)
  result = (a*b) + (c*d)
  if result % 2 == 1:
    totalOdd = totalOdd + 1

print(totalOdd/10000000)