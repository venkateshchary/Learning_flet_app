import flet as ft


def main(page: ft.page):
    def saved_msg(e):
        msg = ft.Text(value="saved")
        if not len(first_name_field.value):
            first_name_field.bgcolor = ft.colors.RED
            first_name_field.update()
        page.add(msg)

    def greet(e):
        greet_column.controls.append(ft.Text(f"hello {first_name_field.value} {last_name_field.value}"))
        print("greet_column: ", greet_column.controls)
        greet_column.update()
        first_name_field.value=''
        last_name_field.value=''
        page.update()
        first_name_field.autofocus=True
    first_name_field = ft.TextField(label="Enter First  name", width=300, autofocus=True)
    last_name_field = ft.TextField(label="Enter Last  name", width=300)
    greet_column = ft.Column()
    # password_field = ft.TextField(label="Enter password", width=300)
    save_button = ft.ElevatedButton(text="say hello", on_click=greet)
    page.add(first_name_field, last_name_field, save_button, greet_column)


ft.app(target=main)
