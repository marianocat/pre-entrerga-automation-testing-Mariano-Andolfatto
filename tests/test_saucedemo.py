from socket import timeout

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import utils.utiles as utiles


@pytest.fixture
def driver():
    """
    Fixture para obtener una instancia del navegador Firefox y cerrarlo después de la prueba.
    Con esto no necesito cerrar el navegador en cada test, ya que se hace automáticamente al finalizar la prueba.
    """
    navegador = utiles.get_driver()
    try:
        yield navegador
    finally:
        navegador.quit()

@pytest.mark.login
def test_login_exitoso(driver):
    utiles.try_login(driver, "standard_user", "secret_sauce")

    titulo = driver.title

    # Validar el URL despues del login
    assert "inventory.html" in driver.current_url
    assert titulo == "Swag Labs"


@pytest.mark.login
def test_login_fallido(driver):
    utiles.try_login(driver, "standard_user", "wrong_password")

    msj_error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    
    msj_error_text = msj_error.text

    # Validar que el mensaje de error sea el esperado
    assert msj_error_text == "Epic sadface: Username and password do not match any user in this service", f"Mensaje incorrecto: {msj_error_text}"
    assert driver.current_url == utiles.URI_LOGIN

@pytest.mark.pagproductos
def test_ctrlProductos(driver):
    """
    Verificamos la presencia de elementos clave (productos, menu)
    """
    utiles.try_login(driver, "standard_user", "secret_sauce")

    
    # Validar que el título de la página sea el esperado
    assert driver.title == "Swag Labs", f"Título incorrecto: {driver.title}"

    productos = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )

    assert len(productos) > 0, "No se encontraron productos en la página de inventario."

    btnMenu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "react-burger-menu-btn"))
    )
    btnCarrito = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-link']"))
    )
    cmbOrdenar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
    )
    contacto = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "social"))
    )

    assert btnMenu.is_displayed(), "El botón de menú no está presente en la página de inventario."
    assert btnCarrito.is_displayed(), "El botón del carrito no está presente en la página de inventario."
    assert cmbOrdenar.is_displayed(), "El combo de ordenar no está presente en la página de inventario."
    assert contacto.is_displayed(), "El contacto no está presente en la página de inventario."

@pytest.mark.carrito
def test_carrito(driver):
    """
    Verificamos que el carrito de compras funcione correctamente.
    """
    utiles.try_login(driver, "standard_user", "secret_sauce")
    utiles.reset_status(driver)

    # Agregar un producto al carrito
    btnAgregar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    btnAgregar.click()

    carritoCantProd = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-badge']"))
    ).text

    assert carritoCantProd == "1", f"La cantidad de productos en el carrito es incorrecta: {carritoCantProd}"

    btnCarrito = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='shopping-cart-link']"))
    )
    btnCarrito.click()

    labelsProductos = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))
    )

    assert "Sauce Labs Backpack" in [label.text for label in labelsProductos], "El producto agregado no se encuentra en el carrito."