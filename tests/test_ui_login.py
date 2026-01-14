import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from utils.config import UI_LOGIN_URL


@pytest.mark.ui
def test_login_invalid_shows_error_message():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        page = LoginPage(driver)
        page.open(UI_LOGIN_URL)
        page.login("wrong_user", "wrong_pass")

        msg = page.get_flash_message()
        assert "Your username is invalid" in msg
    finally:
        driver.quit()
