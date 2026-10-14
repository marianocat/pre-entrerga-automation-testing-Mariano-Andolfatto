from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URI_LOGIN = "https://www.saucedemo.com/"
URI_INVENTORY = "https://www.saucedemo.com/inventory.html"


def try_login(driver, usuario, password):
    """
    Función para realizar el login en la página de prueba.
    """
    # Localizar elementos
    input_usuario = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    input_password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    boton_login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )

    # Completar el formulario
    input_usuario.send_keys(usuario)
    input_password.send_keys(password)

    # Hacer login
    boton_login.click()

def reset_status(driver):
    """
    Función para resetear el estado de la aplicación.
    """
    # Localizar y hacer clic en el menú
    menu_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    )
    menu_button.click()

    # Localizar y hacer clic en el botón de reset
    reset_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "reset_sidebar_link"))
    )
    reset_button.click()