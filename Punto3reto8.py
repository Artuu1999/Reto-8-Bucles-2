n = int(input("Ingrese numero natural: "))
for n in range (n, 2, -2):
  if n%2 == 0:
     print(n)
  else:
     print (n-1)