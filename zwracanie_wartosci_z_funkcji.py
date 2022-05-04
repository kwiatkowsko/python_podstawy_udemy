def PrintAnimal(animal=''):
    # this function prints a cat, bear or bat
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

    if animal == 'cat':
        print(txt_cat)
    elif animal == 'bear':
        print(txt_bear)
    elif animal == 'bat':
        print(txt_bat)
    else:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)
        return False

    return True


if PrintAnimal():
    print('The parameter was correct')
else:
    print('The parameter was incorrect')

if PrintAnimal('dog'):
    print('The parameter was correct')
else:
    print('The parameter was incorrect')

if PrintAnimal('bat'):
    print('The parameter was correct')
else:
    print('The parameter was incorrect')

from datetime import date


def DaysToEndOfYear(year=date.today().year,
                    month=date.today().month,
                    day=date.today().day):
    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    return delta.days


print('Date: 2020-12-20 days to end of year: %d' % (DaysToEndOfYear(2020, 12, 20)))

print('Date: 2020-12-21 days to end of year: %d' % (DaysToEndOfYear(2020, 12, 21)))

print('Date: TODAY days to end of year: %d' % (DaysToEndOfYear()))
