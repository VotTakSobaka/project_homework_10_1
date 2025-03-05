from typing import List, Dict
import datetime

def filter_by_state(data: List[Dict[str, str]], state: str) -> List[Dict[str, str]]:
    """Фильтрует данные по состоянию."""
    return [item for item in data if item.get("state") == state]

def sort_by_date(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Сортирует данные по дате."""
    for item in data:
        try:
            datetime.datetime.strptime(item["date"], "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Неверный формат даты: {item['date']}")
    return sorted(data, key=lambda x: x["date"])
