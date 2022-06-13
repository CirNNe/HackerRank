# Let's learn about list comprehensions! You are given three integers x, y, and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i+j+k is not equal to n.

def listComprehensions(x=0, y=0, z=0, n=0):
  temporary_list = []
  for i in range(0, x+1):
    for j in range(0, y+1):
      for k in range(0, z+1):
        temporary_list.append([i,j,k])
  result = [v for v in temporary_list if sum(v) != n] # list comprehensions
  return result


x = int(input('Valor de x: '))
y = int(input('Valor de y: '))
z = int(input('Valor de z: '))
n = int(input('Valor de n: '))
print(listComprehensions(x, y, z, n))
