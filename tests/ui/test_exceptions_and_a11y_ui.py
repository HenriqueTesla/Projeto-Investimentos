from playwright.sync_api import Page, expect
from pages.navbar_component import NavbarComponent
from pages.portfolio_page import PortfolioPage


def test_cadastro_com_formulario_vazio(
    logged_page: Page,
    navbar: NavbarComponent,
    portfolio_page: PortfolioPage,
):
    navbar.navegar_para_carteira()

    portfolio_page.tentar_cadastrar_formulario_vazio()

    expect(
        portfolio_page.linhas_tabela_carteira.filter(
            has_text="Nenhum ativo cadastrado"
        )
    ).to_be_visible(timeout=5000)


def test_cadastro_com_quantidade_negativa(
    logged_page: Page,
    navbar: NavbarComponent,
    portfolio_page: PortfolioPage,
):
    navbar.navegar_para_carteira()

    portfolio_page.cadastrar_aporte(
        ativo="Poupança",
        quantidade="-200",
        preco="1.00",
        dias_inv="30",
        dias_plan="180",
    )

    expect(
        portfolio_page.alerta_erro
    ).to_be_visible(timeout=5000)


def test_cadastro_com_preco_negativo(
    logged_page: Page,
    navbar: NavbarComponent,
    portfolio_page: PortfolioPage,
):
    navbar.navegar_para_carteira()

    portfolio_page.cadastrar_aporte(
        ativo="Poupança",
        quantidade="1000",
        preco="-1.00",
        dias_inv="30",
        dias_plan="180",
    )

    expect(
        portfolio_page.alerta_erro
    ).to_be_visible(timeout=5000)


def test_verificar_campos_desabilitados(
    logged_page: Page,
    navbar: NavbarComponent,
    portfolio_page: PortfolioPage,
):
    navbar.navegar_para_carteira()

    assert (
        portfolio_page.campo_quantidade_desabilitado()
        or portfolio_page.campo_preco_desabilitado()
    ) is False


def test_acessibilidade_imagens_com_alt(
    logged_page: Page,
    navbar: NavbarComponent,
    portfolio_page: PortfolioPage,
):
    navbar.navegar_para_carteira()

    portfolio_page.verificar_imagens_com_alt()
