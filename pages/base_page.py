from playwright.sync_api import Page, Locator


class BasePage:

    def __init__(self, page: Page, base_url: str = ""):
        self.page = page
        self.base_url = base_url

    def navegar(self, path: str = ""):
        url_destino = f"{self.base_url}/{path}".rstrip("/")
        self.page.goto(
            url_destino if url_destino else self.base_url
        )

    def obter_titulo(self) -> str:
        return self.page.title()

    def recarregar(self):
        self.page.reload()
