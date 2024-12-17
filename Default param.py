def send_email(message, recipient, * , sender = 'university.help@gmail.com') :
    j = 0
    x = []
    z = 0

    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return
    for z in ( recipient , sender ):
        for i in ( '.com', '.net' ,'.ru' ):
            if i in z [-3:]:
                j = j + 1
                x = z.replace( i , '' )
            elif i in z [-4:]:
                j = j + 1
                x = z.replace ( i, '')
        if '@' in x[1: len(x) -1]:
            j = j + 1
    if j != 4:
        print('Невозможно отправить письмо с адреса ', sender, 'на адрес ', recipient)
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса ', sender , 'на адрес ', recipient )
    else: print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender ,  'на адрес ', recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
