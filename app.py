from datetime import datetime

import flet as ft

from components import AppDropdown, AppTextField, PrimaryButton
from models import Task, User
from services import ReportService


class TaskManagerApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.started_at = datetime.now()
        self.current_user = None
        self.time_in = None

        self.tasks = [
            Task(1, "Read OOP notes", 3),
            Task(2, "Finish Flet project", 3),
            Task(3, "Prepare presentation", 2),
            Task(4, "Check homework", 1),
            Task(5, "Send project to teacher", 2),
        ]

        self.root = ft.Column(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        self.login_field = AppTextField(
            label="Login",
            width=320,
            autofocus=True,
        )

        self.login_message = ft.Text("")

        self.task_field = AppTextField(
            label="New task",
            width=360,
        )

        self.priority_dropdown = AppDropdown(
            label="Priority",
            width=150,
            value="1",
            options=[
                ft.DropdownOption(key="1", text="Low"),
                ft.DropdownOption(key="2", text="Medium"),
                ft.DropdownOption(key="3", text="High"),
            ],
        )

        self.filter_dropdown = AppDropdown(
            label="Filter",
            width=160,
            value="all",
            options=[
                ft.DropdownOption(key="all", text="All"),
                ft.DropdownOption(key="active", text="Active"),
                ft.DropdownOption(key="done", text="Completed"),
            ],
            on_select=self.change_filter,
        )

        self.task_list = ft.Column(
            spacing=8,
            width=720,
        )

        self.progress = ft.ProgressBar(
            width=720,
            value=0,
        )

        self.stats_text = ft.Text("")
        self.info_text = ft.Text("")

    def start(self):
        self.page.title = "Simple Task Manager"
        self.page.padding = 24
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window.width = 900
        self.page.window.height = 720
        self.page.window.prevent_close = True
        self.page.window.on_event = self.on_window_event

        self.page.add(self.root)
        self.show_login()

    def show_login(self):
        self.root.controls = [
            ft.Container(height=80),
            ft.Icon(ft.Icons.ACCOUNT_CIRCLE, size=72),
            ft.Text("Task Manager", size=30, weight=ft.FontWeight.BOLD),
            ft.Text("Enter your login to continue"),
            self.login_field,
            PrimaryButton(
                content="Sign in",
                icon=ft.Icons.LOGIN,
                on_click=self.login,
                width=180,
            ),
            self.login_message,
        ]
        self.page.update()

    def login(self, e):
        login = (self.login_field.value or "").strip()

        if not login:
            self.login_message.value = "Enter a login"
            self.page.update()
            return

        self.current_user = User(1, login)
        self.time_in = datetime.now()
        self.show_main()

    def show_main(self):
        self.root.controls = [
            ft.Row(
                controls=[
                    ft.Icon(ft.Icons.CHECKLIST, size=34),
                    ft.Column(
                        controls=[
                            ft.Text(
                                "My tasks",
                                size=28,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Text(f"User: {self.current_user.login}"),
                        ],
                        spacing=2,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Divider(),
            ft.Container(
                content=ft.Row(
                    controls=[
                        self.task_field,
                        self.priority_dropdown,
                        PrimaryButton(
                            content="Add",
                            icon=ft.Icons.ADD,
                            on_click=self.add_task,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                padding=12,
                border_radius=12,
                bgcolor=ft.Colors.GREY_100,
            ),
            ft.Row(
                controls=[
                    self.filter_dropdown,
                    ft.OutlinedButton(
                        content="Sort by priority",
                        icon=ft.Icons.SORT,
                        on_click=self.sort_tasks,
                    ),
                    ft.TextButton(
                        content="Clear completed",
                        on_click=self.clear_completed,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            self.progress,
            self.stats_text,
            ft.Divider(),
            self.task_list,
            self.info_text,
        ]

        self.render_tasks()

    def add_task(self, e):
        title = (self.task_field.value or "").strip()

        if not title:
            self.info_text.value = "Task title is empty"
            self.page.update()
            return

        next_id = max(task.id for task in self.tasks) + 1 if self.tasks else 1
        priority = int(self.priority_dropdown.value or "1")

        self.tasks.append(Task(next_id, title, priority))
        self.task_field.value = ""
        self.info_text.value = "Task added"
        self.render_tasks()

    def toggle_task(self, task: Task):
        task.completed = not task.completed
        self.render_tasks()

    def delete_task(self, task: Task):
        self.tasks.remove(task)
        self.info_text.value = "Task deleted"
        self.render_tasks()

    def clear_completed(self, e):
        self.tasks = [task for task in self.tasks if not task.completed]
        self.info_text.value = "Completed tasks cleared"
        self.render_tasks()

    def change_filter(self, e):
        self.render_tasks()

    def sort_tasks(self, e):
        self.tasks.sort()
        self.info_text.value = "Tasks sorted"
        self.render_tasks()

    def get_visible_tasks(self) -> list[Task]:
        selected = self.filter_dropdown.value

        if selected == "active":
            return [task for task in self.tasks if not task.completed]

        if selected == "done":
            return [task for task in self.tasks if task.completed]

        return list(self.tasks)

    def render_tasks(self):
        self.task_list.controls.clear()

        for task in self.get_visible_tasks():
            title = ft.Text(
                task.title,
                size=16,
                weight=ft.FontWeight.W_500,
            )

            details = ft.Text(
                f"Priority: {task.priority}",
                size=12,
                color=ft.Colors.GREY_700,
            )

            card = ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Checkbox(
                            value=task.completed,
                            on_change=lambda e, item=task: self.toggle_task(item),
                        ),
                        ft.Column(
                            controls=[title, details],
                            spacing=2,
                            expand=True,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINE,
                            tooltip="Delete",
                            on_click=lambda e, item=task: self.delete_task(item),
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=12,
                border_radius=10,
                bgcolor=(
                    ft.Colors.GREEN_50
                    if task.completed
                    else ft.Colors.WHITE
                ),
            )

            self.task_list.controls.append(card)

        completed = sum(1 for task in self.tasks if task.completed)
        total = len(self.tasks)

        self.progress.value = completed / total if total else 0
        self.stats_text.value = f"Completed: {completed} / {total}"

        if not self.task_list.controls:
            self.task_list.controls.append(
                ft.Text(
                    "No tasks",
                    text_align=ft.TextAlign.CENTER,
                )
            )

        self.page.update()

    async def on_window_event(self, e: ft.WindowEvent):
        if e.type != ft.WindowEventType.CLOSE:
            return

        time_out = datetime.now()
        login = (
            self.current_user.login
            if self.current_user is not None
            else "not_logged_in"
        )
        time_in = self.time_in or self.started_at

        ReportService.save(login, time_in, time_out)
        await self.page.window.destroy()
