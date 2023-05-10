s = int(input("Введите количество билетов: "))
cash = 0
for i in range(1, s + 1):
    age = int(input("Введите возраст: "))
    if age < 18:
        print("Бесплатный билет")
    elif 18 <= age <= 25:
        print("Стоимость билета 990")
        cash = 990 + cash
    else:
        print("Стоимость билета 1390")
        cash = 1390 + cash
if s > 3:
    cash = cash*0.9
print("Сумма к оплате: ", cash)
