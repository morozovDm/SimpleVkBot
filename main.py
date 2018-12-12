import requests
import vk_api  #импортируем библиотеку vk.api
import Cesar  #импортируем код Цезаря
import Vigenere  #импортируем код Виженера
from vk_api.longpoll import VkLongPoll, VkEventType  #подключились к библиотеке vkLongpoll
from random import randint

MassMessage = ["", "", "", "", ""]
myToken = '42bbc69ab47986956cf1744e80695f41da04b6e9c7b21698d2e0c346cc79ea68555f8b8331224dced1a28'
session = requests.Session()
vk_session = vk_api.VkApi(token=myToken)
vk = vk_session.get_api()


def write_msg(userId, text):
    vk.messages.send(
        user_id=userId, 
        message=text, 
        random_id=randint(0, 100000000))


def main():
    longpoll = VkLongPoll(vk_session)
    global MassMessage  # присвоили переменной MassMessages глобальное значение

    while True:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    if MassMessage[0] == "":
                        MassMessage[0] = "ЧоКавоПрограммисты"
                        write_msg(
                            event.user_id,
                            "Привет, укажи метод шифрования Цезаря или Виженера"
                        )
                        break
                    if MassMessage[1] == "":
                        if event.text == "Цезарь" or event.text == "Цезаря" or event.text == "Виженер" or event.text == "Виженера" or event.text == "виженер" or event.text == "виженера" or event.text == "цезарь" or event.text == "цезаря":
                            MassMessage[1] = event.text
                            write_msg(event.user_id,
                                      "Зашифровать или расшифровать?")
                            break
                        else:
                            write_msg(event.user_id, "Не понял")
                    if MassMessage[2] == "" and MassMessage[1] != "":
                        if event.text == "зашифровать" or event.text == "расшифровать" or event.text == "Расшифровать" or event.text == "Зашифровать":
                            MassMessage[2] = event.text
                            write_msg(event.user_id, "Напиши текст сообщения")
                            break
                        else:
                            write_msg(event.user_id, "what do you mean, dude?")
                    if MassMessage[3] == "" and MassMessage[2] != "":
                        MassMessage[3] = event.text
                        if MassMessage[1] == "Виженер" or MassMessage[
                                1] == "Виженера" or MassMessage[
                                    1] == "виженера" or MassMessage[
                                        1] == "виженер":
                            write_msg(event.user_id, "Укажи ключ")
                            break
                    if MassMessage[4] == "" and MassMessage[3] != "":
                        MassMessage[4] = event.text
                        write_msg(event.user_id,
                                  "making calculations :3 :3 :3")
                        Raschet(event)
                        break


def Raschet(event):
    if MassMessage[1] == "Цезарь" or MassMessage[1] == "Цезаря" or MassMessage[
            1] == "цезаря" or MassMessage[1] == "цезарь":
        if MassMessage[2] == "зашифровать" or MassMessage[2] == "Зашифровать":
            write_msg(event.user_id, Cesar.encrypt_cesar((MassMessage[3]), 3))
        if MassMessage[2] == "расшифровать" or MassMessage[2] == "Расшифровать":
            write_msg(event.user_id, Cesar.decrypt_cesar((MassMessage[3]), -3))

    if MassMessage[1] == "Виженер" or MassMessage[
            1] == "Виженера" or MassMessage[1] == "виженера" or MassMessage[
                1] == "виженер":
        if MassMessage[2] == "зашифровать" or MassMessage[2] == "Зашифровать":
            write_msg(
                event.user_id,
                Vigenere.encrypt_vigenere(MassMessage[3], MassMessage[4]))
        if MassMessage[2] == "расшифровать" or MassMessage[2] == "Расшифровать":
            write_msg(
                event.user_id,
                Vigenere.decrypt_vigenere(MassMessage[3], MassMessage[4]))

    MassMessage[0] = ""
    MassMessage[1] = ""
    MassMessage[2] = ""
    MassMessage[3] = ""
    MassMessage[4] = ""


if __name__ == '__main__':
    main()
