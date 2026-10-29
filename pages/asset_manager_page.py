from playwright.sync_api import Page, Locator, expect
from pages.base_page import BasePage


class AssetManagerPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.tabela_taxas = page.locator(
            "[data-testid='table-asset-rates']"
        )

        self.linhas_taxas = self.tabela_taxas.locator("tbody tr")

        self.mensagem_sucesso = page.locator(
            "[data-testid='rates-success']"
        )

    def aguardar_tabela(self):
        expect(self.tabela_taxas).to_be_visible()

    def aguardar_ativos(self):
        expect(self.linhas_taxas.first).to_be_visible(
            timeout=15000
        )

    def contar_ativos(self) -> int:
        return self.linhas_taxas.count()

    def obter_linha_por_ativo(self, nome_ativo: str) -> Locator:
        return self.linhas_taxas.filter(
            has_text=nome_ativo
        ).first

    def obter_campo_taxa(self, nome_ativo: str) -> Locator:
        return self.obter_linha_por_ativo(
            nome_ativo
        ).get_by_role("textbox")

    def obter_botao_salvar(self, nome_ativo: str) -> Locator:
        return self.obter_linha_por_ativo(
            nome_ativo
        ).get_by_role(
            "button",
            name="Salvar Alteração"
        )

    def salvar_alteracoes(self):
        self.obter_botao_salvar(
            "Poupança"
        ).click()
