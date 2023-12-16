import flet as ft


def main(page: ft.page):
    page.title = "Controls on text box check box dropdown"

    def validate_details(e):
        if not text_box_fn.value and not text_box_ln.value:
            text_box_fn.error_text = "please enter first name"
            page.update()
        else:
            fname = text_box_fn.value
            page.clean()
            page.add(ft.Text(F"HELLO {fname} {text_box_ln.value} {gender.value}"))

    def terms_cond(e):
        output_t.value = "Read terms and conditions"
        page.update()

    text_box_fn = ft.TextField(label="Enter your first name", autofocus=True)
    text_box_ln = ft.TextField(label="Enter your last name")
    text_box_pswd = ft.TextField(label="password")
    gender = ft.Dropdown(options=[ft.dropdown.Option("Female"),
                                  ft.dropdown.Option("Male"),
                                  ft.dropdown.Option("Others")
                                  ])
    submit = ft.ElevatedButton(text="Submit", on_click=validate_details)
    output_t = ft.Text(value="")
    check_b = ft.Checkbox(label="Read terms & Conditions", on_change=terms_cond)
    page.add(text_box_fn, text_box_ln, gender, text_box_pswd, check_b,submit, output_t)


ft.app(target=main)
