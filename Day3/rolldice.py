from random import randint

face = randint(1, 6)

if face == 1:
  result = 'Sing a song'
elif face == 2:
  result = 'Dance'
elif face == 3:
  result = 'Imitate dog'
elif face == 4:
  result = 'Do push up'
elif face == 5:
  result = 'Say a quote'
else:
  resul = 'Tell a joke'

print(result)