import flet as ft


def main(page: ft.Page):
    page.title = "Test login app"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    user_image = ft.Icon(name=ft.icons.PERSON, size=100)
    user_input = ft.TextField(label="Enter user name", on_focus=True, width=300, height=200)
    user_pswd = ft.TextField(label="Enter password", width=300, height=200, password=True)

    # page.horizontal_alignment = "center"
    # page.vertical_alignment = "center"
    # row1 = Row([Container(
    #     bgcolor=colors.AMBER_700,
    #     content=TextField(value="", on_focus=True),
    #     width=400,
    #     height=500,
    #     padding=20
    # )],alignment=ft.MainAxisAlignment.CENTER)
    # page.add(row1)
    # user = ft.Row([
    #     ft.Icon(name=ft.icons.PERSON, size=100),
    #     user_input
    # ], alignment=ft.MainAxisAlignment.CENTER
    # )
    page.add(user_image, user_input, user_pswd)


ft.app(target=main)
