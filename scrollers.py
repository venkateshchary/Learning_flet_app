import flet as ft


def main(page: ft.page):
    page.title = "scrolling example"
    for i in range(100):
        t_field = ft.Text(value=f"{i}")
        page.controls.append(t_field)
    page.scroll = "always"
    page.update()


ft.app(target=main)