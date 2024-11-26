cont =  0

n = int(input("Digite um número para saber se ele é primo: "))

while n <= 0:
    n = int(input("Digite um número inteiro maior que 0 por favor-: "))

for i in range(n, 0, -1):
    if n % i == 0:
        cont += 1
if cont > 2:
    print(f"{n} não é primo")
else:print(f"{n} é primo")
