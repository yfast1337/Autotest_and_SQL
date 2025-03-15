# Алексей Рогачев, 27А когорта — Финальный проект. Инженер по тестированию плюс

import new_requests
import data


# объявление функции для позитивной проверки получения ранее созданного заказа по его номеру
def positive_assert(body_order):
    creation_response = new_requests.create_new_order(body_order) # создание заказа
    track_num = new_requests.get_order_track(creation_response) # получение номера заказа подставляя ответ при создании заказа
    get_order_response = new_requests.get_order_by_track(track_num) # запрос заказа по ранее полученному номеру
    assert get_order_response.status_code == 200



# объявление функции для позитивного теста получения заказа по номеру
def test_get_order_by_track_positive_response():
    positive_assert(data.BODY_ORDER)