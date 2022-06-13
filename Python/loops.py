# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i².
# n = 3
# The list of non-negative integers that are less than n = 3 is [0, 1, 2]. Print the square of each number on a separate line.

def loops(n=0):
  arr = list()
  for v in range(0, n):
    arr.append(v)
  for i in arr:
    result = i ** 2
    print(result)


n = int(input('Digite o valor: '))
loops(n)
