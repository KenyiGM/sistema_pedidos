from datetime import datetime
from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    cantidad: int

class ProductoVista(ProductoBase):
    id: int
    activo: bool

class ProductoCrear(ProductoBase):
    pass

class ProductoActualizar(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int
    activo: bool
    fecha_creacion: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True


