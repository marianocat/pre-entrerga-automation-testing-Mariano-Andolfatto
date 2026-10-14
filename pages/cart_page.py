from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage: 
    _CART_ITEMS = (By.CLASS_NAME, "cart_item") 
    _ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name") 
    _CHECKOUT_BUTTON = (By.ID, "checkout") 
    _CONTINUE_SHOPPING = (By.ID, "continue-shopping") 
    _TITULO = (By.CSS_SELECTOR, "[data-test='title']")
    _REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='remove']") 

    def __init__(self, driver): 
        self.driver = driver 
        self.wait = WebDriverWait(driver, 10) 
        # Verificar que estamos en la página correcta 
        self.wait.until(EC.url_contains("cart.html")) 

    def obtener_titulo_solapa(self) -> str:
        """Obtiene el título de la solapa de login."""
        return self.driver.title

    def obtener_titulo(self) -> str:
        """Obtiene el título de la solapa de login."""
        return self.wait.until(EC.visibility_of_element_located(self._TITULO)).text


    def obtener_url(self) -> str:
        """Obtiene la URL de la página."""
        return self.driver.current_url

    def obtener_productos_en_carrito(self): 
        """Obtiene la lista de productos en el carrito.""" 
        return self.driver.find_elements(*self._CART_ITEMS) 

    def obtener_numero_productos(self): 
        """Obtiene el número de productos en el carrito.""" 
        return len(self.obtener_productos_en_carrito())

    def quitar_primer_producto(self): 
        """Quita el primer producto del carrito.""" 
        remove_button = self.wait.until(EC.visibility_of_all_elements_located(self._REMOVE_BUTTONS))[0] 
        remove_button.click() 
        return self 
    
    def obtener_nombres_productos(self): 
        """Obtiene los nombres de todos los productos en el carrito.""" 
        elementos_nombre = self.driver.find_elements(*self._ITEM_NAMES) 
        return [elemento.text for elemento in elementos_nombre] 

    def continuar_comprando(self): 
        """Regresa a la página de inventario.""" 
        self.driver.find_element(*self._CONTINUE_SHOPPING).click() 
        from pages.inventory_page import InventoryPage 
        return InventoryPage(self.driver) 

    def proceder_checkout(self): 
        """Inicia el proceso de checkout.""" 
        self.driver.find_element(*self._CHECKOUT_BUTTON).click() 
        # Aquí podrías devolver CheckoutPage cuando la implementes 
        return self