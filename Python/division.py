# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,  a//b . The second line should contain the result of float division,  a/b .
# No rounding or formatting is necessary.

def division(a=0, b=0):
  integer_division = a // b
  float_division = a / b
  print(integer_division)
  print(float_division)


a = int(input('Valor de a: '))
b = int(input('Valor de b: '))
division(a, b)
