import streamlit as st
import os
import random
from PIL import Image

# Configuración de estilo CSS
page_bg_css = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #FFF9E3;  /* Cambia este color al que prefieras */
}

body, [data-testid="stAppViewContainer"] {
    color: #040423;  /* Cambia este color al que prefieras */
}

[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);  /* Esto oculta el fondo del header */
}

[data-testid="stSidebar"] {
    background-color: #040423;  /* Cambia el color del sidebar */
}

h1, h2, h3, h4, h5, h6 {
    color: #333333;  /* Cambia este color al que prefieras, #333333 es un gris oscuro */
}

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

.justified-text {
    text-align: justify;
}
</style>
"""

# Insertar el CSS en la aplicación
st.markdown(page_bg_css, unsafe_allow_html=True)

# Título de la aplicación
st.title("GAN para Terapia Cognitiva y Salud Mental")
st.write("Proyecto para la clase de Computación Cognitiva.")
st.write("Dr. Harold Vazquez")
st.write("Integrantes: Steven Newton, Enrique Soto, Diego Hernandez")

# Descripción del proyecto
st.markdown("""
<div class="justified-text">
            
### Objetivo del Proyecto
El proyecto busca desarrollar una prueba de concepto (PoC) que demuestre cómo las Redes Generativas Antagónicas (GAN) 
pueden ser utilizadas para crear contenido visual terapéutico adaptativo, diseñado específicamente para abordar las 
necesidades emocionales y cognitivas individuales de los pacientes. Al proporcionar una herramienta que permita a 
los terapeutas personalizar las sesiones de terapia de manera más precisa y dinámica, se espera mejorar los resultados 
terapéuticos y aumentar la satisfacción de los pacientes. El sistema buscará no solo producir contenido adaptado a las 
necesidades individuales de los pacientes, sino también integrar una interfaz interactiva que permita a terapeutas y pacientes 
interactuar de manera efectiva con la plataforma, proporcionándoles herramientas adicionales para mejorar la experiencia terapéutica. 

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
1. *Selección de Imágenes:* El usuario debe seleccionar exactamente 5 imágenes haciendo clic en las casillas de verificación correspondientes a las imágenes que más resuenen con sus sentimientos o que consideren más relevantes para su sesión de terapia.
2. *Confirmación de la selección:* Una vez seleccionadas las 5 imágenes, el usuario puede revisar su selección. Las imágenes seleccionadas se mostrarán en una vista previa ampliada, permitiendo al usuario asegurarse de que estas son las que desean enviar al modelo GAN.
3. *Procesamiento por el GAN:* El modelo GAN generará una imagen aleatoria basada en el dataset ganador.
4. *Visualización y Uso del Contenido Generado:* La imagen generada por el modelo GAN se mostrará en la pantalla. Esta imagen pretende a futuro ser utilizada por el terapeuta y el paciente para explorar temas adicionales, reflexionar sobre emociones o como punto de partida para actividades terapéuticas personalizadas.
</div>
""", unsafe_allow_html=True)

# Cargar las imágenes del grid
image_folder = 'images/gridImages'
images = {
    "Art": ["art1.png", "art2.png", "art3.png", "art4.png"],
    "Butterfly": ["butterfly1.png", "butterfly2.png", "butterfly3.png", "butterfly4.png"],
    "Flower": ["flower1.png", "flower2.png", "flower3.png", "flower4.png"],
    "Landscape": ["landscape1.png", "landscape2.png", "landscape3.png", "landscape4.png"]
}

# Mostrar las imágenes en un grid de 4x4
selected_images = []
st.write("### ¿Con que imagenes te sientes identificado hoy? Selecciona hasta 5 imágenes:")

cols = st.columns(4)

for idx, (category, image_list) in enumerate(images.items()):
    for i, image_name in enumerate(image_list):
        img_path = os.path.join(image_folder, image_name)
        img = Image.open(img_path).resize((300, 300))  # Redimensiona la imagen a 300x300 px
        with cols[i % 4]:
            if st.checkbox(" ", key=f"{category}_{i}"):
                selected_images.append(category)
            st.image(img, use_column_width=True)

# Contar cuántas imágenes fueron seleccionadas por categoría
dataset_count = {category: selected_images.count(category) for category in images.keys()}

# Obtener el dataset ganador
max_count = max(dataset_count.values())
winning_datasets = [k for k, v in dataset_count.items() if v == max_count]

if len(selected_images) == 5:
    st.write(f"Has seleccionado 5 de 5 imágenes.")
    if len(winning_datasets) == 1:
        winning_dataset = winning_datasets[0]
        #st.write(f"El dataset ganador es: {winning_dataset}")
    else:
        winning_dataset = random.choice(winning_datasets)
        #st.write(f"El dataset ganador es: {winning_dataset} (Empate, seleccionado al azar)")

    # Selección aleatoria de una imagen generada
    gan_image_folder = f"images/PretrainedGanImg/{winning_dataset}"
    gan_images = os.listdir(gan_image_folder)
    selected_gan_image = random.choice(gan_images)
    gan_image_path = os.path.join(gan_image_folder, selected_gan_image)

    if st.button("Enviar al GAN"):
        st.write("El GAN procesará las imágenes del dataset y generará una nueva imagen.")
        st.image(gan_image_path, caption="Imagen generada por el GAN", use_column_width=True)

elif len(selected_images) > 5:
    st.write("Has seleccionado más de 5 imágenes. Por favor, selecciona solo 5.")
else:
    st.write("Por favor, selecciona exactamente 5 imágenes.")
