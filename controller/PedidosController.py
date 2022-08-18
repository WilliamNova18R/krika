#clase Acciones esta clase es la encargada de controlar las opciones e iconos del menu dependiendo del rol del usuario

class Pedidos:
    #se crean los dos atributos en los cuales es estableceran las acciones y los iconos del menus
    def __init__(self) -> None:
        super().__init__()
        self.cola = []
        self.entransito = []
        self.reparto = []
        self.llego = []

    def agregar_pedido(self, obj):
        self.cola.append(obj)

    def listarPedidos(self):
        usuarioHora = ['']
        for i in self.cola:
            nombre = i.usuario + ' / ' + str(i.hora)
            usuarioHora.append(nombre)
        return usuarioHora

    def listarPedidosT(self):
        usuarioHora = ['']
        for i in self.entransito:
            nombre = i.usuario + ' / ' + str(i.hora)
            usuarioHora.append(nombre)
        return usuarioHora

    def listarPedidosR(self):
        usuarioHora = ['']
        for i in self.reparto:
            nombre = i.usuario + ' / ' + str(i.hora)
            usuarioHora.append(nombre)
        return usuarioHora

    def listarPedidosLL(self):
        usuarioHora = ['']
        for i in self.reparto:
            nombre = i.usuario + ' / ' + str(i.hora)
            usuarioHora.append(nombre)
        return usuarioHora

    def agregar_transito(self, obj):
        self.entransito.append(obj)

    def agregar_reparto(self, obj):
        self.reparto.append(obj)

    def agregar_entregado(self, obj):
        self.llego.append(obj)
