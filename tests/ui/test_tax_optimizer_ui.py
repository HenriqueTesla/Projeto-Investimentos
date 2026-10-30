from playwright.sync_api import Page, expect
from pages.tax_optimizer_page import TaxOptimizerPage
from pages.navbar_component import NavbarComponent


def test_analise_fiscal_resgate(
    logged_page: Page,
    navbar: NavbarComponent,
    tax_page: TaxOptimizerPage
):

    navbar.navegar_para_otimizador_fiscal()

    tax_page.analisar_resgate("5000")

    expect(tax_page.resultado_analise).to_be_visible(
        timeout=10000
    )


def test_destaque_melhor_opcao_menor_ir(
    logged_page: Page,
    navbar: NavbarComponent,
    tax_page: TaxOptimizerPage
):

    navbar.navegar_para_otimizador_fiscal()

    tax_page.analisar_resgate("5000")

    expect(tax_page.melhor_opcao).to_be_visible(
        timeout=10000
    )
