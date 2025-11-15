import pytest
from backend.repository.producto_repository import ProductoRepository
from backend.service.producto_service import ProductoService
from backend.model.producto import Producto

@pytest.fixture
def producto_repository(session):
    return ProductoRepository(session)

@pytest.fixture
def producto_service(producto_repository):
    return ProductoService(producto_repository)

def test_obtener_todos_los_productos(producto_service):
    assert len(producto_service.obtener_todos_los_productos()) == 0

def test_obtener_producto_por_id(producto_service):
    assert producto_service.obtener_producto_por_id(1) is None

def test_obtener_producto_por_nombre(producto_service):
    assert producto_service.obtener_producto_por_nombre("Monitor") is None

def test_crear_producto(producto_service):
    nuevo_producto = Producto(
        nombre="PC",
        descripcion="PC para desarrollo de software",
        precio=2100.00,
        cantidad=2
    )
    producto_creado = producto_service.crear_producto(nuevo_producto)
    assert producto_creado is not None

def test_actualizar_producto(producto_service):
    nuevo_producto = Producto(
        nombre="PC",
        descripcion="PC para desarrollo de software",
        precio=2100.00,
        cantidad=2
    )
    producto_creado = producto_service.crear_producto(nuevo_producto)

    producto_creado.nombre = "Monitor"

    producto_actualizado = producto_service.actualizar_producto(producto_creado.id, producto_creado)

    assert producto_actualizado is not None

def test_eliminar_producto(producto_service):
    nuevo_producto = Producto(
        nombre="PC",
        descripcion="PC para desarrollo de software",
        precio=2100.00,
        cantidad=2
    )
    producto_creado = producto_service.crear_producto(nuevo_producto)

    producto_eliminado = producto_service.eliminar_producto(producto_creado.id)

    assert producto_eliminado

def test_desactivar_producto(producto_service):
    nuevo_producto = Producto(
        nombre="PC",
        descripcion="PC para desarrollo de software",
        precio=2100.00,
        cantidad=2
    )
    producto_creado = producto_service.crear_producto(nuevo_producto)

    producto_desactivado = producto_service.desactivar_producto(producto_creado.id)

    assert producto_desactivado.activo is False


    