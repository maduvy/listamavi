n1 = float(input("digite um numero: "))
n2 = float(input("digite outro numero: "))
n3 = float(input("digite mais um numero: "))
if n1 > n2 or n1 > n3:
    print("{} foi o maior numero digitado.".format(n1,n2,n3))
elif n2 > n1 or n2 > n3:
    print("{} foi o maior numero digitado.".format(n1,n2,n3))
else:
    print("{} foi o maior numero digitado".format(n1,n2,n3))