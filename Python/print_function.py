# Without using any string methods, try to print the following: 123...n

def printFunction(n):
  for v in range(1, n+1):
    print(v, end='')


n = int(input('Digite o valor: '))
printFunction(n)
