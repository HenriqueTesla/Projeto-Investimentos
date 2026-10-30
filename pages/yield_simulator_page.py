from playwright.sync_api import Page, Locator, expect
from pages.base_page import BasePage


class YieldSimulatorPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.secao_simulador = page.locator(
            "[data-testid='section-yield-simulator']"
        )

        self.input_meses = page.locator(
            "[data-testid='input-sim-months']"
        )

        self.botao_simular = page.locator(
            "[data-testid='btn-calc-monthly']"
        )

        self.tabela_projecao_mensal = page.locator(
            "[data-testid='table-monthly-projection']"
        )

        self.tabela_resumo_tipos = page.locator(
            "[data-testid='table-type-summary']"
        )

    def informar_periodo(self, meses: int):
        if not 1 <= meses <= 60:
            raise ValueError(
                "O período deve estar entre 1 e 60 meses."
            )

        self.input_meses.wait_for(state="visible")
        self.input_meses.fill("")
        self.input_meses.fill(str(meses))

    def executar_simulacao(self):
        self.botao_simular.click()

        expect(
            self.tabela_projecao_mensal
        ).to_be_visible(timeout=15000)

        expect(
            self.tabela_resumo_tipos
        ).to_be_visible(timeout=15000)

    def simular(self, meses: int):
        self.informar_periodo(meses)
        self.executar_simulacao()

    def obter_tabela_projecao(self) -> Locator:
        return self.tabela_projecao_mensal

    def obter_tabela_resumo(self) -> Locator:
        return self.tabela_resumo_tipos

    def obter_quantidade_meses_renderizados(self) -> int:
        return self.tabela_projecao_mensal.locator(
            "tbody tr"
        ).count()
