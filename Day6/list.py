def example1():
  list1 = [1, 3, 5, 7, 100]
  print(list1)
  list2 = ['hello'] * 5
  print(list2)

  print(len(list1))
  print(list1[0]) # 1
  print(list1[4]) # 100
  # print(list1[5]) # IndexError: list index out of range
  print(list1[-1]) # 100
  print(list1[-3]) # 5

  list1[2] = 300
  print(list1)

  # Add element
  list1.append(200)
  list1.insert(1, 400)
  list1 += [1000, 2000]
  print(list1)
  print(len(list1))

  # Delete element
  list1.remove(3)
  if 1234 in list1:
    list1.remove(1234)
  del list1[0]
  print(list1)

  list1.clear()
  print(list1)

def example2():
  fruits = ['grape', 'apple', 'strawberry', 'waxberry']
  fruits += ['pitaya', 'pear', 'mango']

  for fruit in fruits:
    print(fruit.title(), end='')
  print()

  fruit2 = fruits[1:4]
  print(fruit2)

  fruit3 = fruits[:]
  print(fruit3)

  fruit4 = fruit3[-3:-1]
  print(fruit4)

  fruit5 = fruits[::-1]
  print(fruit5)

if __name__ == '__main__':
  example1()
  example2()