def main():
  set1 = {1, 2, 3, 3, 3, 2}
  print(set1)
  print('Length = ', len(set1))

  set2 = set(range(1, 10))
  print(set2)
  set1.add(4)
  set1.add(5)
  print('set1 = ', set1)
  set2.update([11, 12])
  print('set2 = ', set2)
  set2.discard(5)
  set2.discard(13)
  # set2.remove(13) will get error if doesn't contain that element
  print('set2 = ', set2)
  if 4 in set2:
    set2.remove(4)

  for elem in set2:
    print(elem ** 2, end= '')
  print()

  set3 = set((1, 2, 3, 3, 2, 1))
  print('set3=', set3)
  print(set3.pop())
  print('set3=', set3)

  print('set1=', set1)
  print('set2=', set2)

  print('set1 & set2=', set1 & set2)
  # print(set1.intersection(set2))
  print('set1 | set2=', set1 | set2)
  # print(set1.union(set2))
  print('set1 - set2=', set1 - set2)
  # print(set1.difference(set2))
  print('set1 ^ set2=', set1 ^ set2)
  # print(set1.symmetric_difference(set2))
  print('set2 <= set1=', set2 <= set1)
  # print(set2.issubset(set1))
  print('set3 <= set1=', set3 <= set1)
  # print(set3.issubset(set1))
  print('set1 >= set2=', set1 >= set2)
  # print(set1.issuperset(set2))
  print('set1 >= set3=', set1 >= set3)
  # print(set1.issuperset(set3))


if __name__ == '__main__':
  main()