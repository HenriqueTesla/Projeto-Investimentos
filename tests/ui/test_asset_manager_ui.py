import pytest
from playwright.sync_api import Page, expect
from pages.navbar_component import NavbarComponent
from pages.asset_manager_page import AssetManagerPage


def test_visualizar_tabela_de_taxas(
    logged_page: Page,
    navbar: NavbarComponent,
):
    respostas_api = []

    def registrar_resposta(response):
        if response.request.resource_type in ("fetch", "xhr"):
            respostas_api.append({
                "status": response.status,
                "url": response.url,
            })

    logged_page.on("response", registrar_resposta)

    navbar.navegar_para_gerenciar_taxas()

    asset_page = AssetManagerPage(logged_page)
    asset_page.aguardar_tabela()

    try:
        expect(
            asset_page.linhas_taxas.first
        ).to_be_visible(timeout=10000)
    except AssertionError:
        print("\nURL atual:", logged_page.url)

        print("\nRespostas da API:")
        for resposta in respostas_api:
            print(
                f"HTTP {resposta['status']} {resposta['url']}"
            )

        print(
            "\nHTML da tabela:",
            asset_page.obter_html_tabela()
        )

        print(
            "\nTexto da página:",
            asset_page.obter_diagnostico_pagina()
        )

        raise

    assert asset_page.contar_ativos() > 0


def test_alterar_taxa_anual(
    logged_page: Page,
    navbar: NavbarComponent,
):
    navbar.navegar_para_gerenciar_taxas()

    asset_page = AssetManagerPage(logged_page)
    asset_page.aguardar_tabela()

    expect(asset_page.tabela_taxas).to_be_visible()


def test_persistencia_taxa_apos_recarregar(
    logged_page: Page,
    navbar: NavbarComponent,
):
    navbar.navegar_para_gerenciar_taxas()

    asset_page = AssetManagerPage(logged_page)
    asset_page.aguardar_tabela()

    expect(asset_page.tabela_taxas).to_be_visible()
