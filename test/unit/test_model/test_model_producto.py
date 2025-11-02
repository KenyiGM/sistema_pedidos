from backend.model.producto import Producto

def test_creacion_producto():
    producto = Producto(
        nombre = "Laptop",
        descripcion = "Laptop para desarrollo de software",
        precio = 2100.00,
        cantidad = 2
    )

    assert producto.nombre == "Laptop"
    assert producto.descripcion == "Laptop para desarrollo de software"
    assert producto.precio == 2100.00
    assert producto.cantidad == 2


def test_verificacion_valores_default_producto():
    producto = Producto(
        nombre = "Laptop",
        descripcion = "Laptop para desarrollo de software",
        precio = 2100.00,
        cantidad = 2
    )
    assert producto.id == None
    assert producto.activo == True


def test_actualizacion_producto():
    producto = Producto(
        nombre = "Laptop",
        descripcion = "Laptop para desarrollo de software",
        precio = 2100.00,
        cantidad = 2
    )
    producto.nombre = "Monitor"
    producto.descripcion = "Monitor de 24 pulgadas"
    producto.precio = 500.00
    producto.cantidad = 5

    assert producto.nombre == "Monitor"
    assert producto.descripcion == "Monitor de 24 pulgadas"
    assert producto.precio == 500.00
    assert producto.cantidad == 5
