import pytest

from pages.login_page import LoginPage

@pytest.mark.login
def test_login_valido(driver):
    """
    Test para verificar el login con credenciales válidas.
    """
    login_page = LoginPage(driver)
    assert login_page.obtener_titulo_solapa() == "Swag Labs"

    # Realizar login con credenciales válidas
    login_page.login_completo("standard_user", "secret_sauce")

    assert "inventory.html" in login_page.obtener_url_actual(), "El login no redirigió a la página de inventario."

@pytest.mark.login
def test_login_fallido(driver):
    """
    Test para verificar el login con credenciales inválidas.
    """
    login_page = LoginPage(driver)
    # Realizar login con credenciales inválidas
    login_page.login_completo("standard_user", "wrong_password")

    # Validar que el mensaje de error sea el esperado
    assert login_page.esta_error_visible(), "El mensaje de error no es visible."
    assert login_page.obtener_mensaje_error() == "Epic sadface: Username and password do not match any user in this service", f"Mensaje incorrecto: {login_page.obtener_mensaje_error()}"
    assert login_page.obtener_url_actual() == login_page._URI_LOGIN, f"El URL cambio cuando no se esperaba. {login_page.driver.current_url}"