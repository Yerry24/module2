def send_email(message, recipient,*, sender = "university.help@gmail.com"):
    if (recipient.find('@') == -1 or not (recipient.rfind('.com') == (len(recipient) - 4) or
                                      recipient.rfind('.ru') == (len(recipient) - 3)  or
                                      recipient.find('.net') == (len(recipient) - 4)) or
            sender.find('@') == -1 or not (sender.rfind('.com') == (len(sender) - 4) or
                                        sender.rfind('.ru') == (len(sender) - 3) or
                                        sender.rfind('.net') == (len(sender) - 4))):
        print("Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient)
        return
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса", sender, "на адрес", recipient + ".")
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " + sender + " на адрес " + recipient +".")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
