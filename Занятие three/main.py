import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from cb_RF import get_course
from wiki import get_article

vk_session = vk_api.VkApi(
    token='vk1.a.E_4pTA3t5bSrfi0HFhiqzIdcUBZipYDK9AOIwxgS4PCVE0qerAOo2hDCDIwJYQu7M53CkVeCHEdnCIqB_V2aGoqZZbmLSV_IyHZRI6AIAR39bEE_sGucdhEhTR9SrWZZqhwZ0y2VXThzzLr2eR0Ibk3I5wCIRkoIY1ZqM7lSOkNhI_hlx8ICwxwZ6pxp3dtxg7xgGP1E1b7kcE33qxivtQ')
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_message = event.text.lower()
        if user_message[0:2] == '-к':
            response = "курс доллара {0} руб. за 1 шт, \nКурс евро {1} руб. за 1 шт.\nКурс юаня {2} руб.за 1 шт.".format(
                get_course("R01235"),
                get_course("R01239"), get_course("R01375")
            )
        elif user_message[0:2] == '-в':
            article = user_message[2:]
            response = f'Вот,что я нашел:\n\n{get_article(article)}'

        else:
            response = 'Не знаю такой команды.'
        vk.messages.send(user_id=event.user_id, message=response, random_id=random.randint(-10**7, 10**7))





