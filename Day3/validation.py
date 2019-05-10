username = input('Please enter username: ')
password = input('Please enter password: ')

if username == 'admin' and password == '123456':
  print('identity validate success')
else:
  print('identity validate failure')