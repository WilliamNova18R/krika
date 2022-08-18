from PIL import Image


#esta funcion es la del menu de inicnio
def inicio(st):
    #se cargan las fotos que se van a usar dentro del home
    img = Image.open( "descarga__1_-removebg-preview.png" )
    img2 = Image.open( "krika.png" )
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.image(img)

    with col3:
        st.write(' ')


    st.markdown("""
    <style>
    .big-font {
        font-size:17px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Programa de la Universidad Javeriana Cali realizado para solucionar del problema logistico de Krika Cosmetics en la realizacion de pedidos</p>', unsafe_allow_html=True)
    col11, col12, col13 = st.columns([4, 10, 1])

    with col11:
        st.write(' ')

    with col12:
        st.image( img2, caption='Software made by William Nova', width=400, )

    with col13:
        st.write(' ')












