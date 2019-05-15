def main():
  t = ('台北', 38, True, '台灣')
  print(t)

  print(t[0])
  print(t[2])

  for member in t:
    print(member)

  # t[0] = '新北' # TypeError

  t = ('曼谷', 20, False, '泰國')
  print(t)

  # convert tuple to list
  person = list(t)
  print(person)
  person[0] = '馬尼拉'
  person[1] = 30
  print(person)
  person[1] = 'ohyeah'
  print(person)

  fruits_list = ['apple', 'banana', 'orange']
  fruits_tuple = tuple(fruits_list)
  print(fruits_tuple)

if __name__ == '__main__':
  main()

