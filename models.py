from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, entity_id: int):
        self.id = entity_id

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        if value < 0:
            raise ValueError("ID cannot be negative")
        self._id = value

    @abstractmethod
    def short_info(self) -> str:
        pass


class User(Entity):
    def __init__(self, entity_id: int, login: str):
        super().__init__(entity_id)
        self.login = login

    @property
    def login(self) -> str:
        return self._login

    @login.setter
    def login(self, value: str):
        value = value.strip()
        if not value:
            raise ValueError("Login cannot be empty")
        self._login = value

    def short_info(self) -> str:
        return self.login

    def __str__(self) -> str:
        return self.login

    def __repr__(self) -> str:
        return f"User(id={self.id}, login='{self.login}')"

    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return False
        return self.id == other.id and self.login == other.login

    def __lt__(self, other) -> bool:
        if not isinstance(other, User):
            return NotImplemented
        return self.login.lower() < other.login.lower()


class Task(Entity):
    def __init__(
        self,
        entity_id: int,
        title: str,
        priority: int = 1,
        completed: bool = False,
    ):
        super().__init__(entity_id)
        self.title = title
        self.priority = priority
        self.completed = completed

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        value = value.strip()
        if not value:
            raise ValueError("Task title cannot be empty")
        self._title = value

    @property
    def priority(self) -> int:
        return self._priority

    @priority.setter
    def priority(self, value: int):
        if value not in (1, 2, 3):
            raise ValueError("Priority must be from 1 to 3")
        self._priority = value

    @property
    def completed(self) -> bool:
        return self._completed

    @completed.setter
    def completed(self, value: bool):
        self._completed = bool(value)

    def short_info(self) -> str:
        state = "done" if self.completed else "active"
        return f"{self.title} | priority {self.priority} | {state}"

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return (
            f"Task(id={self.id}, title='{self.title}', "
            f"priority={self.priority}, completed={self.completed})"
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, Task):
            return False
        return (
            self.id == other.id
            and self.title == other.title
            and self.priority == other.priority
            and self.completed == other.completed
        )

    def __lt__(self, other) -> bool:
        if not isinstance(other, Task):
            return NotImplemented
        return (-self.priority, self.title.lower()) < (
            -other.priority,
            other.title.lower(),
        )

    def __le__(self, other) -> bool:
        return self == other or self < other

    def __gt__(self, other) -> bool:
        if not isinstance(other, Task):
            return NotImplemented
        return not self <= other

    def __ge__(self, other) -> bool:
        if not isinstance(other, Task):
            return NotImplemented
        return not self < other
