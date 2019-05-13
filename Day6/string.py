def main():
  string1 = 'hello, world!'
  print(len(string1)) # 13
  print(string1.capitalize()) # Hello, world!
  print(string1.upper()) # HELLO, WORLD!
  print(string1.find('or')) # 8
  print(string1.find('shit')) # -1

  print(string1.startswith('He')) # False
  print(string1.startswith('hel')) # True
  print(string1.endswith('!')) # True
  print(string1.center(50, '*'))
  print(string1.rjust(50, ' '))

  string2 = 'abc123456'
  print(string2[2]) # c
  print(string2[2:5]) # c12
  print(string2[2:]) # c123456
  print(string2[2::2]) # c246
  print(string2[::2]) # ac246
  print(string2[::-1]) # 654321cba
  print(string2[-3:-1]) #45

  print(string2.isdigit()) # False
  print(string2.isalpha()) # False
  print(string2.isalnum()) # True

  string3 = ' xsw@gmail.com '
  print(string3)
  print(string3.strip())

if __name__ == "__main__":
  main()

