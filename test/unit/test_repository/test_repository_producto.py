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
        nombre="Monitor",
        descripcion="Monitor 24 pulgadas",
        precio=800.00,
        cantidad=3
    )
    producto_creado = producto_repository.crear(nuevo_producto)
    producto_buscado = producto_repository.obtener_por_id(producto_creado.id)
    assert producto_buscado is not None
    assert producto_buscado.nombre == "Monitor"

def test_obtener_producto_por_nombre(producto_repository):
    nuevo_producto =  Producto(
        nombre="PC",
        descripcion="PC para desarrollo de software",
        precio=2100.00,
        cantidad=2
    )
    producto_creado = producto_repository.crear(nuevo_producto)
    producto_buscado = producto_repository.obtener_por_nombre(producto_creado.nombre)
    assert producto_buscado is not None
    assert producto_buscado.nombre == "PC"


def test_obtener_todos_los_productos(producto_repository):
    producto1 = Producto(nombre="Mouse", descripcion="Mouse óptico", precio=50.00, cantidad=10)
    producto2 = Producto(nombre="Teclado", descripcion="Teclado mecánico", precio=150.00, cantidad=5)
    producto_repository.crear(producto1)
    producto_repository.crear(producto2)

    assert len(producto_repository.obtener_todos()) > 0

def test_actualizar_producto(producto_repository):
    nuevo_producto = Producto(
        nombre="Tablet",
        descripcion="Tablet de dibujo",
        precio=900.00,
        cantidad=4
    )
    producto_creado = producto_repository.crear(nuevo_producto)
    producto_creado.nombre = "Tablet Pro"

    producto_actualizado = producto_repository.actualizar(producto_creado.id, producto_creado)
    assert producto_actualizado.nombre == "Tablet Pro"

def test_eliminar_producto(producto_repository):
    nuevo_producto = Producto(
        nombre="Impresora",
        descripcion="Impresora multifunción",
        precio=600.00,
        cantidad=1
    )
    producto_creado = producto_repository.crear(nuevo_producto)
    
    producto_eliminado = producto_repository.eliminar(producto_creado.id)
    assert producto_eliminado is True

    producto_buscado = producto_repository.obtener_por_id(producto_creado.id)
    assert producto_buscado is None