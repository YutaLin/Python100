def is_prime(num):
  for factor in range(2, num):
    if num % factor == 0:
      return False
  return True if num != 1 else False

print(is_prime(7))
print(is_prime(18))