import os

import flet as ft
from flet.auth.providers import GitHubOAuthProvider

GITHUB_CLIENT_ID = "9d493b3ebc2389f1af18"  # os.getenv("GITHUB_CLIENT_ID")
assert GITHUB_CLIENT_ID, "set GITHUB_CLIENT_ID environment variable"
GITHUB_CLIENT_SECRET = "e07fb3c5b3560ae2e82fd6564673784d5428201e"  # os.getenv("GITHUB_CLIENT_SECRET")
assert GITHUB_CLIENT_SECRET, "set GITHUB_CLIENT_SECRET environment variable"


def main(page: ft.Page):
    provider = GitHubOAuthProvider(
        client_id=GITHUB_CLIENT_ID,
        client_secret=GITHUB_CLIENT_SECRET,
        redirect_url="http://localhost:8550/api/oauth/redirect",
    )

    def login_click(e):
        page.login(provider)

    def on_login(e):
        print("Login error:", e.error)
        print("Access token:", page.auth.token.access_token)
        print("User ID:", page.auth.user.id)
        page.client_storage.set("user_id", page.auth.user.id)
        page.client_storage.set("token", page.auth.token.access_token)
        page.add(ft.Text(value="logged in successfuly.."))
        user_id = page.client_storage.get("user_id")
        token = page.client_storage.get("token")
        page.add(ft.Text(f"userid:{user_id} | token: {token}"))
        page.update()

    page.on_login = on_login
    page.add(ft.ElevatedButton("Login with GitHub", on_click=login_click))


ft.app(target=main, port=8550, view=ft.WEB_BROWSER)
