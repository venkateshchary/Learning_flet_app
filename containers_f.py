import flet as ft


def main(page: ft.Page):
    page.title = "Containers with background color"
    page.scroll = "always"

    c1 = ft.Container(
        content=ft.ElevatedButton("Elevated Button in Container"),
        bgcolor=ft.colors.YELLOW,
        padding=5,
    )

    c2 = ft.Container(content=ft.ElevatedButton("Elevated Button with opacity=0.5 in Container"),
                      bgcolor=ft.colors.AMBER_300,
                      opacity=1,
                      padding=10,
                      width=400,
                      height=500)
    c3 = ft.Container(content=ft.ElevatedButton("Elevated Button with opacity=0.5 in Container border radius"),
                      bgcolor=ft.colors.AMBER_300,
                      opacity=1,
                      padding=10,
                      width=400,
                      height=500,
                      border_radius=50)

    r = ft.Row([ft.Container(content=ft.Text("Non clickable"),
                             border_radius=10,
                             bgcolor=ft.colors.BLUE_200,
                             height=100,
                             width=200,
                             padding=20),
                ft.Container(content=ft.Text("Clickable wihtout link"),
                             border_radius=10,
                             bgcolor=ft.colors.RED,
                             height=100,
                             width=200,
                             padding=20,
                             on_click=lambda e: print("Clickable without link")),
                ft.ElevatedButton(text="test"),
                # ink =True will add shade animation on click
                ft.Container(content=ft.Text("clickable with link"),
                             bgcolor=ft.colors.YELLOW_900,
                             width=200,height=100, padding=40,
                             ink=True,
                             alignment=ft.alignment.center,
                             on_click = lambda e: print("clickable transparent with link"))

                ],
               alignment=ft.MainAxisAlignment.CENTER, )
    # flet.alignment module: top_left, top_center, top_right,
    # center_left, center, center_right,
    # bottom_left, bottom_center, bottom_right.

    page.add(c1, c2, c3, r)


ft.app(target=main)
