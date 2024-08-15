import streamlit as st
from PIL import Image
import random
from collections import Counter

# CSS personalizado para cambiar el color de fondo, el color del texto y justificar el texto
page_bg_css = """
<style>
/* Cambiar color de fondo */
[data-testid="stAppViewContainer"] {
    background-color: #FFF9E3;  /* Cambia este color al que prefieras */
}

/* Cambiar color del texto */
body, [data-testid="stAppViewContainer"] {
    color: #040423;  /* Cambia este color al que prefieras */
}

[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);  /* Esto oculta el fondo del header */
}

[data-testid="stSidebar"] {
    background-color: #040423;  /* Cambia el color del sidebar */
}

/* Cambiar color de los encabezados */
h1, h2, h3, h4, h5, h6 {
    color: #333333;  /* Cambia este color al que prefieras, #333333 es un gris oscuro */
}

/* Justificar el texto */
.justified-text {
    text-align: justify;
}

/* Estilizar el botón */
div.stButton > button {
    background-color: #FFB6C1; /* Color de fondo del botón (rosa claro pastel) */
    color: #FFFFFF; /* Color del texto */
    padding: 10px 20px; /* Espaciado interno del botón */
    border-radius: 12px; /* Bordes redondeados */
    border: 2px solid #FF69B4; /* Borde del botón (rosa más fuerte pastel) */
    font-size: 16px; /* Tamaño de la fuente */
    font-weight: bold; /* Texto en negrita */
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Sombra del botón */
    cursor: pointer; /* Cambiar el cursor al pasar sobre el botón */
}
div.stButton > button:hover {
    background-color: #FFC0CB; /* Color de fondo al pasar el ratón (rosa pastel más claro) */
    border-color: #FF69B4; /* Mantener el color del borde al pasar el ratón */
}
</style>
"""
# Insertar el CSS en la aplicación
st.markdown(page_bg_css, unsafe_allow_html=True)

# Explicación del proyecto
st.title("GAN para terapia cognitiva y salud mental")
st.write("Proyecto para la clase de Computacion Cognitiva.")
st.write("Dr. Harold Vazquez")
st.write("Integrantes: Steven Newton, Enrique Soto, Diego Hernandez")

# Descripción del proyecto con texto justificado
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

### Propósito  del Proyecto
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
2. *Confirmación de la selección*: Una vez seleccionadas las 5 imágenes, el usuario puede revisar su selección. Las imágenes seleccionadas se mostrarán en una vista previa ampliada, permitiendo al usuario asegurarse de que estas son las que desean enviar al modelo GAN.
3. *Procesamiento por el GAN*: El modelo GAN generará una serie de nuevas imágenes que reflejan los temas, colores y emociones presentes en las imágenes seleccionadas. Estas imágenes se mostrarán al usuario al finalizar el proceso.
4. *Visualización y Uso del Contenido Generado*: Las imágenes generadas por el modelo GAN se mostrarán en la pantalla. Estas imágenes pueden ser utilizadas por el terapeuta y el paciente para explorar temas adicionales, reflexionar sobre emociones o como punto de partida para actividades terapéuticas personalizadas.
            
El modelo producirá nuevas imágenes que tratan de imitar la imagen de referencia o crean variaciones completamente nuevas.
</div>
""", unsafe_allow_html=True)

# Definir los datasets y sus imágenes
datasets = {
    "Mariposas": ["images/gridImages/butterfly1.png", "images/gridImages/butterfly2.png", "images/gridImages/butterfly3.png", "images/gridImages/butterfly4.png"],
    "Wildlife Animals": ["images/gridImages/wildlife1.png", "images/gridImages/wildlife2.png", "images/gridImages/wildlife3.png", "images/gridImages/wildlife4.png"],
    "Art Images": ["images/gridImages/art1.png", "images/gridImages/art2.png", "images/gridImages/art3.png", "images/gridImages/art4.png"],
    "Pets": ["images/gridImages/pet1.png", "images/gridImages/pet2.png", "images/gridImages/pet3.png", "images/gridImages/pet4.png"],
    "Flowers": ["images/gridImages/flower1.png", "images/gridImages/flower2.png", "images/gridImages/flower3.png", "images/gridImages/flower4.png"],
    "Human Face Emotions": ["images/gridImages/emotion1.png", "images/gridImages/emotion2.png", "images/gridImages/emotion3.png", "images/gridImages/emotion4.png"]
}

# Crear una lista de todas las imágenes con sus datasets correspondientes
images = [(dataset, image) for dataset, images in datasets.items() for image in images]
random.shuffle(images)  # Barajar las imágenes para mostrarlas en orden aleatorio

# Mostrar las imágenes en un grid de 6x4
st.write("### Selecciona hasta 5 imágenes:")

# Lista para almacenar las imágenes seleccionadas
selected_images = []

# Crear una cuadrícula de 6x4 usando st.columns
cols = st.columns(4)

# Recorrer las imágenes y colocarlas en la cuadrícula
for idx, (label, img) in enumerate(images.items()):
    resized_img = img.resize((220, 220))  # Redimensionar la imagen a 220x220 píxeles

    # Mostrar la imagen y el checkbox en la columna correspondiente
    with cols[idx % 4]:
        if st.checkbox("", key=label):
            if len(selected_images) < 5:
                selected_images.append(label)
            else:
                st.warning("Ya has seleccionado 5 imágenes.")

        st.image(resized_img, use_column_width=True)

# Mostrar cuántas imágenes se han seleccionado, fuera del bucle para evitar duplicación
st.write(f"Has seleccionado {len(selected_images)} de 5 imágenes.")

# Validar si ya se han seleccionado 5 imágenes
if len(selected_images) == 5:
    st.write("Puedes proceder con el siguiente paso.")
else:
    st.write("Selecciona hasta 5 imágenes para continuar.")
