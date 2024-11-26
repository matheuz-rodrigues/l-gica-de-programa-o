from math import factorial

n = int(input("Digite um número para ver seu fatorial: "))
fatorial=1

'''fatorial = factorial(n)
print(fatorial)'''

for i in range(n, 0, -1):
    fatorial = fatorial*i
print(fatorial)