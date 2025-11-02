import pytest
from backend.repository.producto_repository import ProductoRepository
from backend.model.producto import Producto


@pytest.fixture
def producto_repository(session):
    return ProductoRepository(session)

def test_crear_producto(producto_repository):
    nuevo_producto = Producto(
        nombre = "Laptop",
        descripcion = "Laptop para desarrollo de software",
        precio = 2100.00,
        cantidad = 2
    )
    producto_creado = producto_repository.crear(nuevo_producto)
    assert producto_creado.id is not None
    assert producto_creado.nombre == "Laptop"
    assert producto_creado.descripcion == "Laptop para desarrollo de software"
    assert producto_creado.precio == 2100.00
    assert producto_creado.cantidad == 2


def test_obtener_producto_por_id(producto_repository):
    nuevo_producto = Producto(
        nombre = "Laptop",
        descripcion = "Laptop para desarrollo de software",
        precio = 2100.00,
        cantidad = 2
    )
    producto_creado = producto_repository.crear(nuevo_producto)
    producto_buscado = producto_repository.obtener_por_id(producto_creado.id)
    assert producto_buscado is not None
    assert producto_buscado.id == 2
    assert producto_buscado.nombre == "Laptop"