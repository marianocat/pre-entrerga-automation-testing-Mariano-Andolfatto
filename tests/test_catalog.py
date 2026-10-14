import pytest

@pytest.mark.productos
def test_productos(usuario_logeado):
    """
    Test para verificar la funcionalidad de agregar productos al carrito.
    """
    from pages.inventory_page import InventoryPage

    # Crear una instancia de la página de inventario
    inventory_page = InventoryPage(usuario_logeado)

    # Verificar que el título de la página sea correcto
    assert inventory_page.obtener_titulo().upper() == "PRODUCTS", "El título de la página no es el esperado."

    # Obtener la lista de productos disponibles
    productos = inventory_page.obtener_productos()
    assert len(productos) > 0, "No se encontraron productos en la página de inventario."

    # Agregar el primer producto al carrito
    inventory_page.agregar_primer_producto()

    # Verificar que el contador del carrito se haya incrementado
    contador_carrito = inventory_page.obtener_contador_carrito()
    assert contador_carrito == 1, f"El contador del carrito debería ser 1, pero es {contador_carrito}."

    # Navegar al carrito y verificar que el producto esté presente
    cart_page = inventory_page.ir_al_carrito()
    assert cart_page.obtener_numero_productos() == 1, "El número de productos en el carrito no es el esperado."