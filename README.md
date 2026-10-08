# Simple Flet 1.0 Task Manager

Небольшой учебный проект для демонстрации ООП и базовых возможностей Flet 1.0.

## Запуск

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Установка:

```bash
pip install -r requirements.txt
python main.py
```

## Что есть в проекте

- вход по логину;
- 5 готовых объектов `Task`;
- добавление задачи;
- отметка выполнения;
- удаление;
- фильтрация;
- сортировка по приоритету;
- очистка выполненных задач;
- отчет `report.txt` при закрытии приложения.

## Соответствие требованиям

1. Все основные сущности описаны классами.
2. `Entity` — абстрактный базовый класс.
3. `Task` и `User` наследуются от `Entity`.
4. `Task` и `User` имеют `__eq__`, `__repr__`, `__str__`.
5. `Task` поддерживает сравнение через `<`, `<=`, `>`, `>=`.
6. Атрибуты сущностей имеют getters и setters через `@property`.
7. `dict` в проекте не используется.
8. В `components.py` переопределены 3 Flet-компонента:
   - `TextField`;
   - `Button`;
   - `Dropdown`.
9. В интерфейсе используется больше 10 UI-компонентов:
   `Column`, `Row`, `Container`, `Text`, `Icon`, `TextField`, `Dropdown`,
   `Button`, `OutlinedButton`, `TextButton`, `Checkbox`, `IconButton`,
   `Divider`, `ProgressBar`.
10. В коллекции `list` изначально хранится 5 объектов `Task`.
11. Основная функциональность реализована методами классов.
12. При закрытии сохраняется `report.txt` с полями:
    `login`, `time_in`, `time_out`.
13. Формат времени:
    `%d.%m.%Y %H:%M:%S`.

## Структура

```text
flet_task_manager/
├── main.py
├── app.py
├── models.py
├── components.py
├── services.py
├── requirements.txt
└── README.md
```

Проект намеренно сделан небольшим, без базы данных и сложной архитектуры.
