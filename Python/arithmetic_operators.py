# Add code to print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

def arithmeticOperators(a=0, b=0):
  sum_result = a + b
  difference_result = a - b
  product_result = a * b
  print(sum_result)
  print(difference_result)
  print(product_result)


a = int(input('Digite o valor de "a": '))
b = int(input('Digite o valor de "b": '))
arithmeticOperators(a, b)
