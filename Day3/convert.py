# convert in and cm

value = float(input('Plase enter value:'))
unit = input('Please enter unit:')

if unit == 'in':
  print('%finch = %fcm' %(value, value*2.54))
elif unit == 'cm':
  print('%fcm = %finch' %(value, value/2.54))
else:
  print('please enter valid unit')