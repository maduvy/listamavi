n1 = float(input("digite sua primeira nota "))
n2 = float(input("digite sua segunda nota "))
media = (n1 + n2) / 2
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")