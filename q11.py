s_ante = float(input("Digite seu salário atual: "))
s_a = 0.0
d_e_s = 0.0
p_d_a = 0.0

if s_ante <= 280:
    p_d_a = 20
elif s_ante <= 750:
    p_d_a = 15
elif s_ante <= 1500:
    p_d_a= 10
else:
    p_d_a = 5

d_e_s = s_ante * (p_d_a / 100)
s_a = s_ante+ d_e_s
print(f"Seu salário antes do reajuste era de R${s_ante:.2f}")
print(f"Seu salário foi aumentado em {p_d_a}%")
print(f"Seu salário foi aumentado em R${d_e_s:.2f}")
print(f"Seu salário atual é de R${s_a:.2f}")