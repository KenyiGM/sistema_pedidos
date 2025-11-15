from backend.repository.producto_repository import ProductoRepository


class ProductoService:

    def __init__(self, producto_repository: ProductoRepository):
        self.producto_repository = producto_repository
    
    def obtener_todos_los_productos(self):
        return self.producto_repository.obtener_todos()
    
    def obtener_producto_por_id(self, producto_id):
        return self.producto_repository.obtener_por_id(producto_id)
    
    def obtener_producto_por_nombre(self, producto_nombre):
        return self.producto_repository.obtener_por_nombre(producto_nombre)

    def crear_producto(self, producto):
        return self.producto_repository.crear(producto)
    
    def actualizar_producto(self, producto_id, producto_actualizado):
        return self.producto_repository.actualizar(producto_id, producto_actualizado)
    
    def desactivar_producto(self, producto_id):
        return self.producto_repository.desactivar(producto_id)
    
    def eliminar_producto(self, producto_id):
        return self.producto_repository.eliminar(producto_id)