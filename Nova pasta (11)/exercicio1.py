lista = []
quantidade = int(input("escreva a quantidade de números que deseja digitar:"))
soma = 0
for i in range(quantidade):
    num = float(input("digite um numero"))
    lista.append(num)
    soma += num
media = soma / quantidade
print(lista)
print("a media da lista a cima é",media)