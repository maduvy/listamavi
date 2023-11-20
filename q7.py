a=float(input('digite um numero'))
b=float(input('digite outro'))
c=int(input('digite mais um'))

if a > b and a >c:
    print("o numero {}".format(a))
elif b >a and a > c:
    print("o valor maior e {}".format(b))
else:
    print("o valor maior e: {}".format(c))