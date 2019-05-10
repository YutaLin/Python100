sum = 0
for x in range(101):
  sum += x
print(sum)

sum = 0
for x in range(1, 101):
  sum += x
print(sum)

sum = 0
for x in range(2, 101, 2):
  sum += x
print(sum)

sum = 0
for x in range(1, 101):
  if x % 2 == 0:
    sum += x
print(sum)