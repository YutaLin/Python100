def factorial(num):
  result = 1
  for n in range(1, num + 1):
    result *= n
  return result

m = int(input('m = '))
n = int(input('n = '))

print(factorial(m))
print(factorial(n))
print(factorial(m-n))