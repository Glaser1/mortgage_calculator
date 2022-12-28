# Mortgage Calculator

## Описание

Калькулятор ипотечных предложений.

----

### Пользовательский сценарий
Клиент вводит следующие данные:
1. Стоимость объекта недвижимости, в рублях без копеек. Тип данных: integer
2. Первоначальный взнос, в рублях без копеек. Тип данных: integer
3. Срок, в годах. Тип данных: integer

В ответ ему приходит массив с объектами ипотечных предложений. В каждом объекте есть следующие данные:
1. Наименование банка. Тип данных: string
2. Ипотечная ставка, в процентах. Тип данных: float
3. Платеж по ипотеке, в рублях без копеек.  Тип данных: integer

----

### Функционал: 
1. Модель для хранения ипотечных предложений.
2. CRUD ипотечных предложений.
3. Фильтрацию ипотечных предложений по введенным параметрам.
4. Рассчет платежей у всех валидных ипотечных предложений.
5. Сортировка ипотечных предложений по ставке и платежу.
6. Тестирование Unittest.

----

### Используемый стек
1) Django.
2) DRF
3) django-filters
4) Docker

----
### Локальный запуск приложения
#### Чтобы поднять контейнеры:
```shell
docker stop $(docker ps -aq)
docker-compose -f docker-compose.yml -f docker-compose.override.yml up --build
```
#### Чтобы зайти внутрь контейнера бекенда:
```shell
docker-compose exec backend sh
```
Сервис будет доступен по адресу [http://localhost:8000/api/offer/](http://localhost:8000/api/offer/)
