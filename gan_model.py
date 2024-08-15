import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt

# Load the trained generator model
generator = load_model('butterflyGAN.h5', custom_objects={'tf': tf})

def generate_and_save_single_image(model, img_size=(128, 128)):
    # Generate a single random noise vector
    noise = tf.random.normal([1, 100])
    
    # Generate a single image from the noise
    generated_image = model(noise, training=False)
    
    # Rescale the image to [0, 255] and convert to uint8
    generated_image = (generated_image * 127.5 + 127.5).numpy().astype(np.uint8)
    
    # Plot and save the image
    plt.figure(figsize=(img_size[0] // 20, img_size[1] // 20))
    plt.imshow(generated_image[0])
    plt.axis('off')
    
    plt.savefig('generated_image.png')
    plt.show()

# Generate and save a single image
generate_and_save_single_image(generator)