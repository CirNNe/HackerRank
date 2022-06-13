# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 != 0:
            leap = True
    if year % 400 == 0:
        leap = True
    return leap


year = int(input('Digite o ano: '))
print(is_leap(year))
