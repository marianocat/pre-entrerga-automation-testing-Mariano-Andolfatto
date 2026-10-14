from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage: 
    _TITLE = (By.CLASS_NAME, "title") 
    _PRODUCTS = (By.CLASS_NAME, "inventory_item") 
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']") 
    _REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='remove']") 
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge") 
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link") 
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn") 
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link") 

    def __init__(self, driver):
        self.driver = driver 
        self.wait = WebDriverWait(self.driver, 10) 
        self.title = self.wait.until(EC.visibility_of_element_located(self._TITLE)) 
        self.products = self.wait.until(EC.visibility_of_all_elements_located(self._PRODUCTS)) 
        self.add_buttons = self.wait.until(EC.visibility_of_all_elements_located(self._ADD_BUTTONS))
        self.cart_badge = None 
        self.cart_link = self.wait.until(EC.element_to_be_clickable(self._CART_LINK)) 
        self.menu_button = self.wait.until(EC.element_to_be_clickable(self._MENU_BUTTON)) 
        self.logout_link = None

    def obtener_titulo(self): 
        """Obtiene el título de la página de inventario.""" 
        return self.wait.until(EC.visibility_of_element_located(self._TITLE)).text 

    def obtener_productos(self): 
        """Obtiene la lista de productos disponibles.""" 
        return self.wait.until(EC.visibility_of_all_elements_located(self._PRODUCTS)) 

    def agregar_primer_producto(self): 
        """Añade el primer producto disponible al carrito.""" 
        primer_boton = self.wait.until(EC.visibility_of_all_elements_located(self._ADD_BUTTONS))[0] 
        primer_boton.click() 
        return self 

    def quitar_primer_producto(self): 
        """Quita el primer producto del carrito.""" 
        remove_button = self.wait.until(EC.visibility_of_all_elements_located(self._REMOVE_BUTTONS))[0] 
        remove_button.click() 
        return self 

    def obtener_contador_carrito(self): 
        """Obtiene el número de productos en el carrito.""" 
        try: 
            badge = self.wait.until(EC.visibility_of_element_located(self._CART_BADGE)) 
            return int(badge.text) 
        except: 
            return 0 

    def ir_al_carrito(self): 
        """Navega a la página del carrito.""" 
        self.wait.until(EC.element_to_be_clickable(self._CART_LINK)).click() 
        # Importación lazy para evitar dependencias circulares 
        from pages.cart_page import CartPage 
        return CartPage(self.driver) 

    def hacer_logout(self): 
        """Cierra la sesión del usuario.""" 
        self.wait.until(EC.element_to_be_clickable(self._MENU_BUTTON)).click() 
        logout_link = self.wait.until( 
            EC.element_to_be_clickable(self._LOGOUT_LINK) 
        ) 
        logout_link.click() 
        
        from pages.login_page import LoginPage 
        
        return LoginPage(self.driver)