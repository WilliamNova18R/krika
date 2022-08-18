from PIL import Image


def soporte( st):
    st.header("Informacion de contacto y soporte")
    # se cargan las fotos que se van a usar dentro del home
    img = Image.open("cel.png")
    img1 = Image.open("correo.png")
    st.write("En caso de cualquier problema o solicitar soporte de cualquier tipo referente al software contarse a los siguientes telefono o whatsapp y correo:")
    col1, col2 = st.columns([0.8, 13])  # con estas columnas comodamos el titulo de la pagina

    with col1:
        st.image(img, width=45)
    with col2:
        st.subheader("3054622892")

    col3, col4 = st.columns([0.8, 13])  # con estas columnas comodamos el titulo de la pagina
    with col1:
        st.image(img1, width=45)
    with col2:
        st.subheader('william84859@hotmail.com')

from PIL import Image
"""Instructions"""

#esta funcion es la del menu de inicnio
def consultar_instrucciones(st):
    #se cargan las fotos que se van a usar dentro del home
    img = Image.open( "logo.png" )
    img2 = Image.open( "PlazoletaJaverianaCali.jpg" )
    col1, col2 = st.columns([1.1, 10]) #con estas columnas comodamos el titulo de la pagina

    with col1:

        st.image(img, width=75)
    with col2:
        st.header("Calificacion de trabajos finales")
    #se imprime la informacion del menu
    st.write("Programa de la Universidad Javeriana Cali realizado para la evaluación de proyectos de grado de posgrado,"
             " creación y descargar de las actas de calificacion")
    st.write( "Dependiendo de tu rol tenemos diferentes acciones para ti:" )
    st.write(" * Asistente -> Inicializar Acta de Evaluación, ver actas creadas y estadisticas de notas ")
    st.write(" * Jurado -> Calificar, Exportar acta, editar calificacion y ver calificaciones realizadas y estadisticas de notas ")
    st.write(" * Director/a -> Modificar los criterios de calificacion y ver las actas creadas y estadisticas de notas")
    st.image( img2, caption='Software made by William Nova' )










