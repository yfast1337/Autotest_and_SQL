import requests
import configuration
import data

# объявление функции создания нового заказа
def create_new_order(BODY_ORDER):
    return requests.post(configuration.URL + configuration.CREATE_ORDER,
                         json=BODY_ORDER,
                         headers=data.HEADERS)


# объявление функции получения номера заказа из ответа формата JSON(из функции create_new_order в виде переменной)
def get_order_track(response):
    return response.json()["track"]


# объявление функции получения ранее созданного заказа по его номеру
def get_order_by_track(track_num):
    return requests.get(configuration.URL + configuration.GET_ORDER + str(track_num))
