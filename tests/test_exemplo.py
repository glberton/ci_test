# import pytest
import logging

from playwright.sync_api import Page, expect

logger = logging.getLogger(__name__)


def test_buscar_google(page: Page):
    logger.info('Abrindo página Google')
    page.goto('https://google.com')
    logger.info('Verificando se o title é Google')
    expect(page).to_have_title('Google')
