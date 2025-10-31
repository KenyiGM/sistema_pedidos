from typing import Optional

from sqlmodel import Field, SQLModel


class Producto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    descripcion: str
    precio: float
    cantidad: int
    activo: bool = True
    fecha_creacion: Optional[str] = None
    fecha_actualizacion: Optional[str] = None
