n = int(input("Введите количество билетов, которые вы хотите купить: "))
print('\n')
summ = 0

for i in range(n):
    print(f"Билет №{i+1}")
    age = int(input("Введите возраст посетителя для данного билета: \n"))
    if age >= 18 and age < 25:
        summ += 990
    elif age >= 25:
        summ += 1390

if n > 3:
    summ *= 0.9

print(f"Итоговая стоимость билетов: {summ}")
