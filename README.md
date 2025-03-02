
# PythonProject

## Описание

Этот проект содержит функции для работы с масками карт и счетов, а также для сортировки данных по датам. Он включает в себя тесты для проверки корректности работы этих функций.


## Функции

### 1. `get_mask_card_number()`

Запрашивает у пользователя номер карты и возвращает его в замаскированном виде.

### 2. `get_mask_account()`

Запрашивает у пользователя номер счета и возвращает его в замаскированном виде.

### 3. `mask_account_card()`

Принимает номер карты или счета и возвращает его в замаскированном виде.

### 4. `get_date()`

Запрашивает у пользователя дату и возвращает её в формате `YYYY-MM-DD`.

### 5. `filter_by_state()`

Фильтрует данные по заданному состоянию.

### 6. `sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]`

Сортирует список словарей по значению ключа `date`. Параметр `reverse` определяет порядок сортировки (по умолчанию по убыванию).

## Тестирование

Для тестирования функций используется библиотека `pytest`. Тесты проверяют корректность работы функций в различных сценариях.

### Запуск тестов

1. Убедитесь, что виртуальное окружение активировано.
2. Запустите тесты с помощью команды: pytest


### Тесты

#### 1. Тесты для `get_mask_card_number` и `get_mask_account`

- Проверяют корректность маскирования номеров карт и счетов.
- Используют мокирование для замены `input()`.

#### 2. Тесты для `mask_account_card`

- Проверяют, что функция правильно маскирует номера карт и счетов.

#### 3. Тесты для `get_date`

- Проверяют, что функция возвращает дату в правильном формате.

#### 4. Тесты для `filter_by_state`

- Проверяют, что функция корректно фильтрует данные по состоянию.

#### 5. Тесты для `sort_by_date`

- Проверяют сортировку по убыванию и возрастанию.
- Проверяют обработку некорректных форматов дат.
- Проверяют работу с пустыми списками и списками с некорректными датами.
=======
# project_homework_10_1

# Фильтрация и Сортировка Данных

Этот проект содержит две функции для работы со списками словарей: `filter_by_state` и `sort_by_date`. Эти функции позволяют фильтровать и сортировать данные по заданным критериям.

## Установка

Для использования функций просто скопируйте код в ваш проект. Не требуется установка дополнительных библиотек.

## Функции

### `filter_by_state(data: list, state: str = 'EXECUTED') -> list`

Функция фильтрует список словарей по значению ключа `state`.

#### Параметры:
- `data`: Список словарей, которые нужно отфильтровать.
- `state`: Значение для ключа `state`, по умолчанию `'EXECUTED'`.

#### Возвращает:
Новый список словарей, отфильтрованный по значению `state`.



### `sort_by_date(data: list, reverse: bool = True) -> list`

Функция сортирует список словарей по значению ключа `date`.

#### Параметры:
- `data`: Список словарей, которые нужно отсортировать.
- `reverse`: Параметр, определяющий порядок сортировки (по умолчанию `True`).

#### Возвращает:
Новый список словарей, отсортированный по дате.


