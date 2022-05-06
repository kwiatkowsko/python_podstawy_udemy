import math
#1° = (π * rad)/180
#1 rad = 180°/π

degree = 360
radian = degree * math.pi / 180
print(radian)
print("%d degree is %f radians" % (degree, radian))
degree = 45
radian = degree * math.pi / 180
print(radian)
print("%d degree is %f radians" % (degree, radian))
print(math.radians(360))
print(math.radians(45))

small_pizza_r = 22
big_pizza_r = 27
family_pizza_r = 38
small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00

small_area = math.pi * small_pizza_r ** 2
big_area = math.pi * big_pizza_r ** 2
family_area = math.pi * family_pizza_r ** 2

print('small', small_pizza_r, small_pizza_price, small_area)
print('big', big_pizza_r, big_pizza_price, big_area)
print('family', family_pizza_r, family_pizza_price, family_area)
print('')
print('small', small_pizza_price / small_area)
print('big', big_pizza_price / big_area)
print('family', family_pizza_price / family_area)
print('')

math_ls = dir(math)
print(math_ls)
