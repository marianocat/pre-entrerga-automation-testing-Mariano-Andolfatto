import pytest

@pytest.mark.carrito
def test_carrito(inv3Prods):
    """
    Test para verificar la funcionalidad del carrito de compras.
    """
    from pages.cart_page import CartPage

    productos_iniciales = inv3Prods.obtener_productos()
    if len(productos_iniciales) == 0:
        pytest.skip("No hay productos disponibles para agregar al carrito.")

    cart_page = inv3Prods.ir_al_carrito()

    assert "cart.html" in cart_page.obtener_url(), "La URL de la página de carrito no es la esperada."
    assert cart_page.obtener_titulo().upper() == "YOUR CART", "El título de la página de carrito no es el esperado."
    assert cart_page.obtener_numero_productos() == 3, "El número de productos en el carrito no es el esperado."

    cart_page.quitar_primer_producto()
    
    assert cart_page.obtener_numero_productos() == 2, "El número de productos en el carrito no es el esperado despues de eliminar uno."

    