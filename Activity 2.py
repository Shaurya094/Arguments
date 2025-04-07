n = int(input("Enter a number divisable by 3: "))

def cube(n):
 return n * n * n

def by3(n):
 if n % 3 == 0:
  return cube(n)
 else:
  return False
 
print(by3(n))