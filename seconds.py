n = int(input("Por favor, entre com o número de segundos que deseja converter: "))

day = n // (24 * 3600)

n = n % (24 * 3600)
hour = n // 3600

n %= 3600
minutes = n // 60

n %= 60
seconds = n

print(day,"dias,",hour,"horas,",minutes,"minutos e",seconds,"segundos.")

#2 dias, 1 horas, 36 minutos e 55 segundos.

