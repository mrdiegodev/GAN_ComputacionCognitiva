import streamlit as st
from PIL import Image
import os
from collections import Counter

# Establecer la carpeta de imágenes
image_folder = 'images/gridImages'

# Cargar todas las imágenes de la carpeta
images = {f"Image {i+1}": Image.open(os.path.join(image_folder, file)) for i, file in enumerate(os.listdir(image_folder))}

# CSS personalizado para justificar el texto y cambiar el color del fondo
page_bg_css = """
<style>
/* Cambiar color de fondo */
[data-testid="stAppViewContainer"] {
    background-color: #F8F4E3;
}

/* Cambiar color del texto */
body, [data-testid="stAppViewContainer"] {
    color: #040423;
}

[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}

[data-testid="stSidebar"] {
    background-color: #040423;
}

/* Cambiar color de los encabezados */
h1, h2, h3, h4, h5, h6 {
    color: #333333;
}

/* Estilo del botón */
div.stButton > button {
    background-color: #FFB6C1;
    color: #FFFFFF;
    padding: 10px 20px;
    border-radius: 12px;
    border: 2px solid #FF69B4;
    font-size: 16px;
    font-weight: bold;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    cursor: pointer;
}
div.stButton > button:hover {
    background-color: #FFC0CB;
    border-color: #FF69B4;
}
</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)

# Justificación del texto
justify_text_css = """
<style>
    .justified-text {
        text-align: justify;
    }
</style>
"""
st.markdown(justify_text_css, unsafe_allow_html=True)

# Título de la aplicación
st.title("GAN para terapia cognitiva y salud mental")
st.write("Proyecto para la clase de Computación Cognitiva.")
st.write("Dr. Harold Vazquez")
st.write("Integrantes: Steven Newton, Enrique Soto, Diego Hernandez")

# Explicación del proyecto
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
1. *Selección de Imágenes:*. El usuario debe seleccionar exactamente 5 imágenes haciendo clic en las casillas de verificación correspondientes a las imágenes que más resuenen con sus sentimientos o que consideren más relevantes para su sesión de terapia.
2. *Confirmación de la selección*: Una vez seleccionadas las 5 imágenes, el usuario puede revisar su selección.
3. *Procesamiento por el GAN*: El modelo GAN generará una serie de nuevas imágenes que reflejan los temas, colores y emociones presentes en las imágenes seleccionadas. Estas imágenes se mostrarán al usuario al finalizar el proceso.
4. *Visualización y Uso del Contenido Generado*: Las imágenes generadas por el modelo GAN se mostrarán en la pantalla. Estas imágenes pueden ser utilizadas por el terapeuta y el paciente para explorar temas adicionales, reflexionar sobre emociones o como punto de partida para actividades terapéuticas personalizadas.
            
El modelo producirá nuevas imágenes que tratan de imitar la imagen de referencia o crean variaciones completamente nuevas.
</div>
""", unsafe_allow_html=True)

# Mostrar las imágenes en una cuadrícula 4x6 con checkboxes
st.write("### Selecciona hasta 5 imágenes:")

# Lista para almacenar las imágenes seleccionadas y su dataset correspondiente
selected_images = []
selected_datasets = []

# Crear una cuadrícula de 4x6 usando st.columns
cols = st.columns(4)

# Recorrer las imágenes y colocarlas en la cuadrícula
for idx, (label, img) in enumerate(images.items()):
    resized_img = img.resize((220, 220))  # Redimensionar la imagen a 220x220 píxeles
    dataset_name = label.split()[1]  # Asumimos que el dataset es parte del nombre de la imagen
    with cols[idx % 4]:
        if st.checkbox("", key=label):
            if len(selected_images) < 5:
                selected_images.append(resized_img)
                selected_datasets.append(dataset_name)
        st.image(resized_img, use_column_width=True)

# Mostrar la cantidad de imágenes seleccionadas
st.write(f"Has seleccionado {len(selected_images)} de 5 imágenes.")

# Validar que se hayan seleccionado exactamente 5 imágenes
if len(selected_images) == 5:
    # Contar las ocurrencias de cada dataset
    dataset_count = Counter(selected_datasets)
    
    # Determinar el dataset ganador
    winning_dataset = max(dataset_count, key=dataset_count.get)
    st.write(f"El dataset ganador es: {winning_dataset}")

    # Botón para enviar al GAN
    if st.button("Enviar al GAN"):
        st.write("El GAN procesará las imágenes del dataset ganador y generará una nueva imagen.")
        # Aquí va la lógica para enviar al GAN (actualmente no está implementada)
else:
    st.write("Por favor, selecciona exactamente 5 imágenes.")
