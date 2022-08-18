import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from controller.CuentaController import Cuentas
from view.sesion import iniciar_sesion, crear_cuenta, crear_cuenta_usuarios, cerrar_sesion
from view.soporte import soporte
from controller.AccionesController import Acciones
from controller.ProductoController import Productos
from controller.KeyController import Keys
from controller.CompraController import Factura
from controller.VentasContoller import Venta
from controller.PedidosController import Pedidos
from view.productos import agregarProducto, seleccionarListado, consultarProducto, editarDatos, eliminarProducto
from view.compras import registrarCompra
from view.Home import inicio
from view.ListaPedidos import pedidos, transito, reparto




class MainView:

    def __init__(self) -> None:
        super().__init__()

        if 'main_view' not in st.session_state:
            self.menu_actual = "sesion"
            self.cuentas_controller = Cuentas()
            self.acciones_controller = Acciones()
            self.productos_controller = Productos()
            self.keys_controller = Keys()
            self.compra_controller = Factura()
            self.venta_controller = Venta()
            self.pedidos_controller = Pedidos()

            st.session_state['main_view'] = self
        else:
            self.menu_actual = st.session_state.main_view.menu_actual
            self.cuentas_controller = st.session_state.main_view.cuentas_controller
            self.acciones_controller = st.session_state.main_view.acciones_controller
            self.productos_controller = st.session_state.main_view.productos_controller
            self.keys_controller = st.session_state.main_view.keys_controller
            self.compra_controller = st.session_state.main_view.compra_controller
            self.venta_controller = st.session_state.main_view.venta_controller
            self.pedidos_controller = st.session_state.main_view.pedidos_controller
             # Carga de las variables necesarias
        self._inicialializar_layout()

    def _inicialializar_layout(self):
        img = Image.open('logo.png')
        # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
        st.set_page_config(page_title="Krika Cosmetics", page_icon=img, layout="wide",
                           initial_sidebar_state="expanded")
        # Defines the number of available columns del area principal
        self.col1, self.col2, self.col3, self.col4, self.col5, self.col6, self.col7 = st.columns([1, 1, 1, 1, 1, 1, 1])

        # Define lo que abrá en la barra de menu
        with st.sidebar:
            self.menu_actual = option_menu("Menu", self.acciones_controller.acciones,
                                           icons=self.acciones_controller.iconos, menu_icon="cast", default_index=0)

    def ver_ejemplo(self):
        pass

    def controlar_menu(self):
        # Filtro opciones de menu
        if self.menu_actual == "sesion":
            iniciar_sesion(st, self.cuentas_controller, self.acciones_controller)
        elif self.menu_actual == "Inicio":
            inicio(st)
        elif self.menu_actual == "Contacto Soporte":
            soporte(st)
        elif self.menu_actual == "Crear Cuenta":
            crear_cuenta(st, self.cuentas_controller, self.keys_controller)
        elif self.menu_actual == "Crear Cuenta Cliente":
            crear_cuenta_usuarios(st, self.cuentas_controller, self.keys_controller)
        elif self.menu_actual == "Cerrar Sesion":
            cerrar_sesion(st, self.acciones_controller)
        elif self.menu_actual == "Agregar Producto":
            agregarProducto(st, self.productos_controller, self.keys_controller)
        elif self.menu_actual == "Inventario":
            seleccionarListado(st, self.productos_controller)
        elif self.menu_actual == "Consultar Producto":
            consultarProducto(st, self.productos_controller, self.keys_controller)
        elif self.menu_actual == "Registrar Compra":
            registrarCompra(st, self.productos_controller, self.keys_controller, self.compra_controller, self.venta_controller, self.pedidos_controller)
        elif self.menu_actual == "Editar Datos Producto":
            editarDatos(st, self.productos_controller, self.keys_controller)
        elif self.menu_actual == "Eliminar Producto":
            eliminarProducto(st, self.productos_controller, self.keys_controller)
        elif self.menu_actual == "Pedidos":
            pedidos(st, self.pedidos_controller, self.keys_controller )
        elif self.menu_actual == "Pedidos Listo":
            transito(st, self.pedidos_controller, self.keys_controller )
        elif self.menu_actual == "En Reparto":
            reparto(st, self.pedidos_controller, self.keys_controller )






# Main call
if __name__ == "__main__":
    gui = MainView()
    gui.controlar_menu()
