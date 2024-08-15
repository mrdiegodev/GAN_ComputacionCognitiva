import streamlit as st
from PIL import Image
import random

# CSS personalizado para justificar el texto
justify_text_css = """
<style>
    .justified-text {
        text-align: justify;
    }
</style>
"""

# Insertar el CSS en la aplicación
st.markdown(justify_text_css, unsafe_allow_html=True)

# Título de la aplicación
st.title("GAN para terapia cognitiva y salud mental")
st.write("Proyecto para la clase de Computación Cognitiva.")
st.write("Dr. Harold Vazquez")
st.write("Integrantes: Steven Newton, Enrique Soto, Diego Hernandez")

# Descripción
st.markdown("""
<div class="justified-text">
### Objetivo del Proyecto
El proyecto busca desarrollar una prueba de concepto (PoC) que demuestre cómo las Redes Generativas Antagónicas (GAN) 
pueden ser utilizadas para crear contenido visual terapéutico adaptativo, diseñado específicamente para abordar las 
necesidades emocionales y cognitivas individuales de los pacientes. Al proporcionar una herramienta que permita a 
los terapeutas personalizar las sesiones de terapia de manera más precisa y dinámica, se espera mejorar los resultados 
terapéuticos y aumentar la satisfacción de los pacientes.  El sistema buscará no solo producir contenido adaptado a las necesidades 
individuales de los pacientes, sino también integrar una interfaz interactiva que permita a terapeutas y pacientes 
interactuar de manera efectiva con la plataforma, proporcionándoles herramientas adicionales 
para mejorar la experiencia terapéutica. 

### Propósito del Proyecto
El propósito de este proyecto es abordar una necesidad crítica en el campo de la salud mental: 
la falta de personalización efectiva en las intervenciones terapéuticas. Actualmente, 
los enfoques tradicionales de la terapia cognitivo-conductual (CBT) a menudo no logran 
adaptarse plenamente a las diversas necesidades individuales de los pacientes. 
Esto puede limitar la eficacia del tratamiento, provocando que algunos pacientes no obtengan los beneficios
esperados y, en algunos casos, abandonen la terapia. 

### ¿Qué es un GAN?
Un GAN es un tipo de modelo de aprendizaje profundo compuesto por dos redes neuronales: un **generador** y un **discriminador**. 
- El **generador** crea imágenes falsas que parecen reales.
- El **discriminador** evalúa estas imágenes para distinguir entre imágenes reales y falsas.
A medida que el GAN entrena, el generador mejora en crear imágenes más realistas, mientras que el discriminador mejora en distinguir las falsas de las reales.

### Uso de la Aplicación
La aplicación de Terapia Cognitiva con GAN está diseñada para ayudar a los terapeutas y pacientes a personalizar el 
contenido terapéutico a través de la selección de imágenes que mejor representen sus emociones, 
experiencias o preferencias. A continuación, se describe cómo utilizar la aplicación:
1. **Selección de Imágenes**: El usuario debe seleccionar exactamente 5 imágenes haciendo clic en las casillas de verificación correspondientes a las imágenes que más resuenen con sus sentimientos o que consideren más relevantes para su sesión de terapia.
2. **Confirmación de la selección**: Una vez seleccionadas las 5 imágenes, el usuario puede revisar su selección. Las imágenes seleccionadas se mostrarán en una vista previa ampliada, permitiendo al usuario asegurarse de que estas son las que desean enviar al modelo GAN.
3. **Procesamiento por el GAN**: El modelo GAN generará una serie de nuevas imágenes que reflejan los temas, colores y emociones presentes en las imágenes seleccionadas. Estas imágenes se mostrarán al usuario al finalizar el proceso.
4. **Visualización y Uso del Contenido Generado**: Las imágenes generadas por el modelo GAN se mostrarán en la pantalla. Estas imágenes pueden ser utilizadas por el terapeuta y el paciente para explorar temas adicionales, reflexionar sobre emociones o como punto de partida para actividades terapéuticas personalizadas.
            
El modelo producirá nuevas imágenes que tratan de imitar la imagen de referencia o crear variaciones completamente nuevas.
</div>
""", unsafe_allow_html=True)

# Cargar las imágenes
images = {
    "Image 1": Image.open("images/gridImages/image1.jpg"),
    "Image 2": Image.open("images/gridImages/image2.jpg"),
    "Image 3": Image.open("images/gridImages/image3.jpg"),
    "Image 4": Image.open("images/gridImages/image4.jpg"),
    "Image 5": Image.open("images/gridImages/image5.jpg"),
    "Image 6": Image.open("images/gridImages/image6.jpg"),
    "Image 7": Image.open("images/gridImages/image7.jpg"),
    "Image 8": Image.open("images/gridImages/image8.jpg"),
    "Image 9": Image.open("images/gridImages/image9.jpg"),
    "Image 10": Image.open("images/gridImages/image10.jpg"),
    "Image 11": Image.open("images/gridImages/image11.jpg"),
    "Image 12": Image.open("images/gridImages/image12.jpg"),
    "Image 13": Image.open("images/gridImages/image13.jpg"),
    "Image 14": Image.open("images/gridImages/image14.jpg"),
    "Image 15": Image.open("images/gridImages/image15.jpg"),
    "Image 16": Image.open("images/gridImages/image16.jpg"),
    "Image 17": Image.open("images/gridImages/image17.jpg"),
    "Image 18": Image.open("images/gridImages/image18.jpg"),
    "Image 19": Image.open("images/gridImages/image19.jpg"),
    "Image 20": Image.open("images/gridImages/image20.jpg"),
    "Image 21": Image.open("images/gridImages/image21.jpg"),
    "Image 22": Image.open("images/gridImages/image22.jpg"),
    "Image 23": Image.open("images/gridImages/image23.jpg"),
    "Image 24": Image.open("images/gridImages/image24.jpg"),
}

# Mostrar las imágenes en una cuadrícula 6x4 con checkboxes
st.write("### Selecciona hasta 5 imágenes:")

# Listas para almacenar las imágenes seleccionadas
selected_images = []

# Crear una cuadrícula de 6x4 usando st.columns
cols = st.columns(4)

# Recorrer las imágenes y colocarlas en la cuadrícula
for idx, (label, img) in enumerate(images.items()):
    with cols[idx % 4]:
        if st.checkbox("", key=label):
            selected_images.append(label)
        st.image(img.resize((220, 220)), use_column_width=True)

# Validar la selección y mostrar el conteo de imágenes seleccionadas
st.write(f"Has seleccionado {len(selected_images)} de 5 imágenes.")

# Si se seleccionan 5 imágenes, se habilita el botón para continuar
if len(selected_images) == 5:
    st.write("Puedes proceder a enviar estas imágenes al modelo GAN.")
    if st.button("Enviar al GAN"):
        # Aquí se colocará la lógica para el GAN
        st.write(f"Estas son las imágenes seleccionadas: {selected_images}")
else:
    st.write("Por favor, selecciona exactamente 5 imágenes para continuar.")
