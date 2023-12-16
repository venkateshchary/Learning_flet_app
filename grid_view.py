import flet as ft
import os
os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


def main(page: ft.page):
    page.title = "Grid view"
    page.theme_mode = ft.ThemeMode.LIGHT
    gv = ft.GridView(expand=True, max_extent=200, child_aspect_ratio=1)
    page.add(gv)
    for i in range(10):
        gv.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(1, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5),
            )
        )
    page.update()




ft.app(target=main)