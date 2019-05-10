import math

radius = float(input('Please input radius: '))
perimeter = 2*math.pi*radius
area = math.pi * radius ** 2

print('Perimeter: %.2f' % perimeter)
print('Area: %.2f' % area)