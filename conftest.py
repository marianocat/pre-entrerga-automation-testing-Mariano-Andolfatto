from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope="function")
def driver():
    """
    Fixture para obtener una instancia del navegador Firefox y cerrarlo después de la prueba.
    """
    options = Options()
    options.add_argument("--headless") #no displayar interfaz grafica
    driver = webdriver.Firefox(options=options)
    try:
        driver.set_window_size(1366, 768)
        yield driver
    finally:
        if driver is not None:
            driver.quit()

@pytest.fixture(scope="function")
def usuario_logeado(driver):
    """
    Fixture para obtener un usuario logeado en la aplicación.
    Usa el boton de reset status de la app para asegurarse de que el usuario esté en un estado limpio antes de cada prueba.
    """
    from pages.login_page import LoginPage
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC

    login_page = LoginPage(driver).login_completo("standard_user", "secret_sauce")
    login_page.driver.find_element(By.ID, "react-burger-menu-btn").click()
    login_page.wait.until(EC.element_to_be_clickable((By.ID, "reset_sidebar_link"))).click()
    login_page.driver.refresh()
    return login_page.driver

@pytest.fixture(scope="function")
def inv3Prods(usuario_logeado):
    """
    Fixture para obtener la página de inventario después de iniciar sesión.
    """
    from pages.inventory_page import InventoryPage
    inventario = InventoryPage(usuario_logeado)
    
    inventario.agregar_primer_producto()
    inventario.agregar_primer_producto()
    inventario.agregar_primer_producto()

    return InventoryPage(usuario_logeado)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Para evitar que se genere el reporte cuando se ejecuta pytest --collect-only
    Eso ocurre al hacer cambios en el IDE como modificar o eliminar archivos
    """
    if config.option.collectonly:
        config.option.htmlpath = None
        return
    
    fecha_hora = datetime.now().strftime("%Y%m%d_%H_%M_%S")
    nombre = f"reports/{fecha_hora}_reporte.html"
    config.option.htmlpath = str(config.rootpath / nombre)
