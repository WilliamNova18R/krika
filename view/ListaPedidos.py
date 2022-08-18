def pedidos(st, PedidosController, keyController):
    st.header('Pedidos en cola')
    listarPedidos = PedidosController.listarPedidos()
    seleccion = st.empty()
    pedido = seleccion.selectbox('Lista de pedidos', listarPedidos, key= keyController.pedidos)
    nombre = 0
    index = 0
    for i in range(len(pedido)):
        if pedido[i] == ' ' and pedido[i + 1] == '/' and pedido[i + 2] == ' ':
            nombre = i
            break
    for j in PedidosController.cola:
        if j.usuario == pedido[:nombre] and j.hora == pedido[nombre + 3:]:
            colNumero, colNombre, colCodigo, colPrecioUnidad, colCantidad, colCosto = st.columns(
                [0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
            with colNumero:
                st.write("Numero")

            with colNombre:
                st.write("Nombre")

            with colCodigo:
                st.write("Codigo")

            with colPrecioUnidad:
                st.write("Precio Unidad")

            with colCantidad:
                st.write("Cantidad")

            with colCosto:
                st.write("Costo")
            index = 0
            for k in j.items:

                with colNumero:
                    st.write("%i." % (index + 1))

                with colNombre:
                    st.write(k.nombre)

                with colCodigo:
                    st.write(k.codigo)

                with colPrecioUnidad:
                    st.write(str(k.precio))

                with colCantidad:
                    st.write(str(round(k.cantidad, 2)))

                with colCosto:
                    st.write(str(k.costo))

            listo = st.button('Pedido Listo')
            if listo:
                j.estado = 'Listo para entregarse al domisiliario'
                keyController.pedidos += 1
                PedidosController.agregar_transito(j)
                PedidosController.cola.pop(index)
                st.success('Pedido actualizado')
        index +=1

def transito(st, PedidosController, keyController):
    st.header('Pedidos en transito')
    listarPedidos = PedidosController.listarPedidosT()
    seleccion = st.empty()
    pedido = seleccion.selectbox('Lista de pedidos', listarPedidos, key= keyController.pedidos)
    nombre = 0
    index = 0
    for i in range(len(pedido)):
        if pedido[i] == ' ' and pedido[i + 1] == '/' and pedido[i + 2] == ' ':
            nombre = i
            break
    for j in PedidosController.entransito:
        if j.usuario == pedido[:nombre] and j.hora == pedido[nombre + 3:]:
            colNumero, colNombre, colCodigo, colPrecioUnidad, colCantidad, colCosto = st.columns(
                [0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
            with colNumero:
                st.write("Numero")

            with colNombre:
                st.write("Nombre")

            with colCodigo:
                st.write("Codigo")

            with colPrecioUnidad:
                st.write("Precio Unidad")

            with colCantidad:
                st.write("Cantidad")

            with colCosto:
                st.write("Costo")
            index = 0
            for k in j.items:

                with colNumero:
                    st.write("%i." % (index + 1))

                with colNombre:
                    st.write(k.nombre)

                with colCodigo:
                    st.write(k.codigo)

                with colPrecioUnidad:
                    st.write(str(k.precio))

                with colCantidad:
                    st.write(str(round(k.cantidad, 2)))

                with colCosto:
                    st.write(str(k.costo))

            listo = st.button('Recoger')
            if listo:
                j.estado = 'En proceso de entrega'
                keyController.pedidos += 1
                PedidosController.agregar_reparto(j)
                PedidosController.entransito.pop(index)
                st.success('Pedido actualizado')
        index +=1

def reparto(st, PedidosController, keyController):
    st.header('Pedidos en transito')
    listarPedidos = PedidosController.listarPedidosR()
    seleccion = st.empty()
    pedido = seleccion.selectbox('Lista de pedidos', listarPedidos, key= keyController.pedidos)
    nombre = 0
    index = 0
    for i in range(len(pedido)):
        if pedido[i] == ' ' and pedido[i + 1] == '/' and pedido[i + 2] == ' ':
            nombre = i
            break
    for j in PedidosController.reparto:
        if j.usuario == pedido[:nombre] and j.hora == pedido[nombre + 3:]:
            colNumero, colNombre, colCodigo, colPrecioUnidad, colCantidad, colCosto = st.columns(
                [0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
            with colNumero:
                st.write("Numero")

            with colNombre:
                st.write("Nombre")

            with colCodigo:
                st.write("Codigo")

            with colPrecioUnidad:
                st.write("Precio Unidad")

            with colCantidad:
                st.write("Cantidad")

            with colCosto:
                st.write("Costo")
            index = 0
            for k in j.items:

                with colNumero:
                    st.write("%i." % (index + 1))

                with colNombre:
                    st.write(k.nombre)

                with colCodigo:
                    st.write(k.codigo)

                with colPrecioUnidad:
                    st.write(str(k.precio))

                with colCantidad:
                    st.write(str(round(k.cantidad, 2)))

                with colCosto:
                    st.write(str(k.costo))

            listo = st.button('Entregar')
            if listo:
                j.estado = 'En proceso de entrega'
                keyController.pedidos += 1
                PedidosController.agregar_entregado(j)
                PedidosController.reparto.pop(index)
                st.success('Pedido actualizado')
        index +=1
