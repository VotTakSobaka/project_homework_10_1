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

