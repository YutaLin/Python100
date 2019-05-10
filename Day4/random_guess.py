import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('Please enter: '))
    if number < answer:
        print('bigger')
    elif number > answer:
        print('smaller')
    else:
        print('Bingo!')
        break
print('Total guess time:%d time(s)' % counter)
if counter > 7:
    print('You need to improve your guessing skill')