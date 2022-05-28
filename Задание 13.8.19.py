a = int(input('количество билетов'))
koeff = 0
if a > 3:
   koeff = 0.9
else:
    koeff = 1.0

price = 0
summa = 0
count = a
for a in range(1, a+1):
    b = int(input('возраст'))
    if b < 18:
        price = 0
        count -= 1
    if 18 <= b <= 25:
        price = 990
        count -= 1
    if 25 < b:
        price = 1390
        count -= 1
    summa += price
print('сумма за билеты: ', summa * koeff, 'руб')