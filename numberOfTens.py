integer = int(input("Digite um número inteiro: "))

if integer < 10:
    print("O dígito das dezenas é 0")

else:
    integer2 = integer%100
    print(integer2//10)

