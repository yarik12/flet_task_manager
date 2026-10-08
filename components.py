from typing import Any

import flet as ft


@ft.control
class AppTextField(ft.TextField):
    filled: bool = True
    fill_color: Any = ft.Colors.BLUE_50


@ft.control
class PrimaryButton(ft.Button):
    bgcolor: Any = ft.Colors.BLUE_600
    color: Any = ft.Colors.WHITE


@ft.control
class AppDropdown(ft.Dropdown):
    filled: bool = True
    fill_color: Any = ft.Colors.BLUE_50
