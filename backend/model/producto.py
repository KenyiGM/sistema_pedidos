from datetime import datetime, timezone
from typing import Optional

from sqlmodel import Field, SQLModel


class Producto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, nullable=False, min_length=2)
    descripcion: str = Field(nullable=False, min_length=4)
    precio: float = Field(nullable=False, ge=0)
    cantidad: int = Field(nullable=False, ge=0)
    activo: bool = Field(default=True)
    fecha_creacion: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    fecha_actualizacion: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
