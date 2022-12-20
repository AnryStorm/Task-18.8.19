ticket_price = 0
ticket_quantity = int(input('Введите общее кол-во билетов: '))
for i in range(ticket_quantity):
    i += 1
    age_for_ticket = int(input(f'Введите возраст для {i} билета: '))
    if age_for_ticket < 18:
            print('Билет бесплатный')
    elif 18 <= age_for_ticket < 25:
            ticket_price += 990
            print('Стоимость билета - 990 руб.')
    else:
            ticket_price += 1390
            print('Стоимость билета - 1390 руб.')

if ticket_quantity > 3:
    ticket_price = ticket_price - ((ticket_price / 100) * 10)
    print(f'Сумма к оплате - {ticket_price} руб. (с учетом скидки 10%, (Вы зарегистрировали больше 3-х человек)!')
else:
    print(f'Сумма к оплате - {ticket_price} руб.')
