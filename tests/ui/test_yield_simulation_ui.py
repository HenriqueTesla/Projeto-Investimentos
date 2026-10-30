from playwright.sync_api import Page, expect
from pages.navbar_component import NavbarComponent
from pages.yield_simulator_page import YieldSimulatorPage


def test_simulacao_rentabilidade_12_meses(
    logged_page: Page,
    navbar: NavbarComponent,
    yield_page: YieldSimulatorPage
):

    navbar.navegar_para_simulador()

    yield_page.simular(12)

    expect(
        yield_page.obter_tabela_projecao()
    ).to_be_visible()

    expect(
        yield_page.obter_tabela_resumo()
    ).to_be_visible()

    expect(
        yield_page.obter_tabela_projecao()
    ).to_contain_text("Mês 1")


def test_simulacao_periodo_minimo(
    logged_page: Page,
    navbar: NavbarComponent,
    yield_page: YieldSimulatorPage
):

    navbar.navegar_para_simulador()

    yield_page.simular(1)

    expect(
        yield_page.obter_tabela_projecao()
    ).to_be_visible()

    expect(
        yield_page.obter_tabela_projecao()
    ).to_contain_text("Mês 1")


def test_simulacao_periodo_maximo(
    logged_page: Page,
    navbar: NavbarComponent,
    yield_page: YieldSimulatorPage
):

    navbar.navegar_para_simulador()

    yield_page.simular(60)

    expect(
        yield_page.obter_tabela_projecao()
    ).to_be_visible()

    expect(
        yield_page.obter_tabela_resumo()
    ).to_be_visible()
