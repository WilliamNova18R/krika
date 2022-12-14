#clase Acciones esta clase es la encargada de controlar las opciones e iconos del menu dependiendo del rol del usuario

class Acciones:
    #se crean los dos atributos en los cuales es estableceran las acciones y los iconos del menus
    def __init__(self) -> None:
        super().__init__()
        self.acciones = ['Inicio', 'sesion', 'Crear Cuenta Cliente' ,'Contacto Soporte', ]
        self.iconos = [ 'person-check']


    #esta metodo sirve para establecer las funciones y acciones que cada tipo de usario tendra disponible en el menu
    def menu_acciones(self, tipo):
        if tipo == 'Dueño':
            self.acciones = ['Inicio', 'Crear Cuenta' , 'Agregar Producto', 'Editar Datos Producto', 'Eliminar Producto', 'Inventario' , 'Consultar Producto', 'Registrar Compra', 'Pedidos' ,'Contacto Soporte', 'Cerrar Sesion']
            self.iconos = ['house']
        elif tipo == 'Cliente':
            self.acciones = ['Inicio', 'Consultar Producto', 'Registrar Compra' ,'Contacto Soporte',
                             'Cerrar Sesion']
            self.iconos = ['house']
        elif tipo == 'Trabajador':
            self.acciones = ['Inicio', 'Consultar Producto','Pedidos Listo', 'En Reparto', 'Contacto Soporte',
                             'Cerrar Sesion']
            self.iconos = ['house']