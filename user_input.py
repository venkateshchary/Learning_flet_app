import flet as ft


def main(page: ft.page):
    page.title = "Form input"
    text_box = ft.TextField(label="value", value="0", autofocus=True, text_align="center")
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def minus(e):
        text_box.value = int(text_box.value) - 1
        text_box.update()
        text_box.autofocus=True

    def add(e):
        text_box.value = int(text_box.value) + 1
        text_box.update()

    rt = ft.Row(controls=[
        ft.IconButton(ft.icons.REMOVE, on_click=minus),
        text_box,
        ft.IconButton(ft.icons.ADD_BOX, on_click=add),

    ], alignment=ft.MainAxisAlignment.CENTER)
    page.add(rt)


ft.app(target=main)
