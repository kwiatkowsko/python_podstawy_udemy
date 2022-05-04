def PrintAnimal(*animals):
    # this function prints a cat, bear or bat ascii-art
    txt_cat = r'''
|\---/|
| o_o |
 \_^_/'''
    txt_bear = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    txt_bat = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''

    for animal in animals:
        if animal == 'cat':
            print(txt_cat)
        elif animal == 'bear':
            print(txt_bear)
        elif animal == 'bat':
            print(txt_bat)
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)

    return


PrintAnimal('cat', 'bat')
print('-------------------------------------')
PrintAnimal('cat', 'bat', 'dog', 'bear')
print('-------------------------------------')
PrintAnimal()

from datetime import date


def DaysToEndOfYear(*dates):
    for date_today in dates:
        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print('Date', date_today, 'days to end of year', delta.days)


DaysToEndOfYear(date(1999, 1, 15))
print('----------------')
DaysToEndOfYear(date(1999, 1, 15), date(2009, 1, 15))
print('----------------')
DaysToEndOfYear(date(1999, 1, 15), date(2009, 1, 15), date(2019, 1, 15))
print('----------------')
DaysToEndOfYear(date(1999, 1, 15), date(2009, 1, 15), date(2019, 1, 15), date.today())
