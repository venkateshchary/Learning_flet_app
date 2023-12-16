import flet as ft
import time


def main(page: ft.Page):
    # t = ft.Text(value="Hello, world!", color="green")
    # print(page)
    # page.controls.append(t)
    # print(page)
    # page.update()
    # print(page)
    t = ft.Text()
    page.add(t)  # it's a shortcut for page.controls.append(t) and then page.update()

    def list_append(e):
        page.add(ft.Checkbox(label=task_details.value))
        task_details.value = ''
        task_details.focus()
        print(task_details.value)
        # task_details.update()

    def button_clicked(e):
        page.add(ft.Text("Clicked!"))

    for i in range(2):
        t.value = f"Step {i}"
        page.update()
        time.sleep(1)
    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )
    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )
    for i in range(1):
        page.controls.append(ft.Text(f"Line {i}"))
        # if i > 4:
        #     page.controls.pop(0)
        page.update()
        time.sleep(0.3)

    page.add(ft.Row(
        controls=[ft.TextField(label="your name!"),
                  ft.ElevatedButton(text='click me to send event', on_click=button_clicked), ]
    ))
    task_details = ft.TextField(label="What is to do ?")
    page.add(ft.Row(controls=[
        task_details,
        ft.ElevatedButton(text="Add to list", on_click=list_append)
    ]))


ft.app(target=main)
