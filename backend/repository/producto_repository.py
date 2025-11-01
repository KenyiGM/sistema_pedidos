from typing import Optional
from sqlmodel import select, Session
from backend.model.producto import Producto

class ProductoRepository:

    def __init__(self, session : Session):
        self.session = session
    
    def obtener_todos(self) -> list[Producto]:
        return self.session.exec(select(Producto)).all()
    
    def obtener_por_id(self, producto_id) -> Optional[Producto]:
        return self.session.get(Producto, producto_id)
    
    def obtener_por_nombre(self, nombre) -> Optional[Producto]:
        return self.session.exec(select(Producto).where(Producto.nombre == nombre)).first()
    
    def crear(self, producto) -> Optional[Producto]:
        try:
            self.session.add(producto)
            self.session.commit()
            self.session.refresh(producto)
            return producto
        except Exception as e:
            self.session.rollback()
            raise e
    
    def actualizar(self, producto_id, producto_actualizado) -> Optional[Producto]:
        producto = self.obtener_por_id(producto_id)
        if not producto:
            return None
        for key, value in producto_actualizado.dict(exclude_unset=True).items():
            setattr(producto, key, value)
        try:
            self.session.add(producto)
            self.session.commit()
            self.session.refresh(producto)
            return producto
        except Exception as e:
            self.session.rollback()
            raise e

    def desactivar(self, producto_id) -> Optional[Producto]:
        producto = self.obtener_por_id(producto_id)
        if not producto:
            return None
        try:
            producto.activo = False
            self.session.add(producto)
            self.session.commit()
            self.session.refresh(producto)
            return producto
        except Exception as e:
            self.session.rollback()
            raise e

    def eliminar(self, producto_id) -> bool:
        producto = self.obtener_por_id(producto_id)
        if not producto:
            return False
        try:
            self.session.delete(producto)
            self.session.commit()
            self.session.refresh(producto)
            return True
        except Exception as e:
            self.session.rollback()
            raise e
