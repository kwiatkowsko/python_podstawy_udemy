name = "Agata"
age = 25
daysInYear = 365
message = '%s is %d years old, so is about %d days old'
print(message % (name,age,age*daysInYear))
name = 'Chris'
age = 17
print(message % (name, age, age*daysInYear))
message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name,age,age*daysInYear))
print('1234567890 divided by 12345 is ',1234567890 // 12345,'and the rest is',1234567890 % 12345)
