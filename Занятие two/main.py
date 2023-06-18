import vk_api
import random
from cb_RF import get_dollar_course
from max_diameter import handle_message


vk = vk_api.VkApi(token='vk1.a.E_4pTA3t5bSrfi0HFhiqzIdcUBZipYDK9AOIwxgS4PCVE0qerAOo2hDCDIwJYQu7M53CkVeCHEdnCIqB_V2aGoqZZbmLSV_IyHZRI6AIAR39bEE_sGucdhEhTR9SrWZZqhwZ0y2VXThzzLr2eR0Ibk3I5wCIRkoIY1ZqM7lSOkNhI_hlx8ICwxwZ6pxp3dtxg7xgGP1E1b7kcE33qxivtQ')


while True:
    messages = vk.method("messages.getConversations", {"count": 20, "filter": "unanswered"})
    if messages['count'] >= 1:
        msg_text = messages['items'][0]['last_message']['text']

        if msg_text.lower() == "курс":
            ans = f"Курс доллара на сегодня составляет {get_dollar_course()} руб."
        else:
            ans = "Неизвестная команда"

        user_id = messages['items'][0]['last_message']['from_id']
        vk.method(
            "messages.send",
            {
                'random_id': random.randint(-10 ** 7, 10 ** 7),
                'user_id': user_id,
                'message': ans
            }


            )


