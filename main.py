import flet as ft

from app import TaskManagerApp


class Program:
    @staticmethod
    def main(page: ft.Page):
        application = TaskManagerApp(page)
        application.start()


if __name__ == "__main__":
    ft.run(Program.main)
