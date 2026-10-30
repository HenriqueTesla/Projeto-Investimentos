from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class TaxOptimizerPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.input_valor_resgate = page.locator(
            "[data-testid='input-withdraw-amount']"
        )

        self.botao_analisar = page.locator(
            "[data-testid='btn-calc-withdrawal']"
        )

        self.resultado_analise = page.locator("table")

        self.melhor_opcao = page.get_by_text("⭐ MELHOR OPÇÃO")

    def informar_valor_resgate(self, valor: str):
        self.input_valor_resgate.fill(valor)

    def executar_analise(self):
        self.botao_analisar.click()

    def analisar_resgate(self, valor: str):
        self.informar_valor_resgate(valor)
        self.executar_analise()

    def obter_resultado(self) -> Locator:
        return self.resultado_analise

    def obter_melhor_opcao(self) -> Locator:
        return self.melhor_opcao