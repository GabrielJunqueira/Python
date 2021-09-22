side1 = int(input("Enter the shortest side: "))
side2 = int(input("Enter the next shortest side: "))
side3 = int(input("Enter the longest side: "))
# lembrar de colocar int para não interpretar como string

result = side1 + side2 > side3

print("These sides can form a triangle is:", result)
# lembrar da vírgula para o uso da variável
