#Importing the libraries

import tensorflow as tf
from tensorflow import keras
import time
import matplotlib.pyplot as plt
import numpy as np
import tensorflow_datasets

#Characters will be processed in batches of 32
batch_size = 32

#Dimensions of characters are 32x32
img_height = 32
img_width = 32

#Creating a tensorflow dataset from the training folder
trainingGen = tf.keras.utils.image_dataset_from_directory(
    'ocr_training/vyanjan_database/Train', #Path to the training folder
    image_size=(img_height, img_width),
    batch_size=batch_size,
    color_mode='grayscale')

#Creating a tensorflow dataset from the testing folder
testingGen = tf.keras.utils.image_dataset_from_directory(
    'ocr_training/vyanjan_database/Test', #Path to the testing folder
    image_size=(img_height, img_width),
    batch_size=batch_size,
    color_mode='grayscale')

class_names = trainingGen.class_names
no_of_classes = len(class_names)

#Creating a function to display the images
def displayImages(images, labels):
    plt.figure(figsize=(10, 10))
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")
    plt.show()

#displayImages(*list(trainingGen.take(1))[0])
#print(trainingGen.class_names)

#Creating a convoluted neural network model through a stack of layers
cnnModel = keras.Sequential([
    #Rescaling image down by a factor of 255 to process image
    keras.layers.Rescaling(1./255, input_shape=(img_height, img_width, 1)),

    keras.layers.Conv2D(32, 3,
     activation='relu',padding='valid'),

    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(64, 3, 
    activation='relu'),

    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(128, 3, 
    activation='relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.Dropout(0.25),

    keras.layers.Flatten(),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(no_of_classes, activation='softmax'),
    ]) 

#Compiling the model
cnnModel.compile(
    optimizer='adam',
    loss="sparse_categorical_crossentropy",
    metrics=['accuracy'])

cnnModel.summary()

#Training the model
startTime = time.time()
trainingProcess = cnnModel.fit(
    trainingGen,
    validation_data = testingGen,
    epochs=10,
    validation_steps=10,
    workers=4,
    verbose=1)
endTime = time.time()
trainingScore = cnnModel.evaluate(testingGen)
print(f"Training time: {endTime - startTime}")
print(f"Testing loss: {trainingScore[0]}")
print(f"Testing accuracy: {trainingScore[1]}")

#Saving the model
cnnModel_json = cnnModel.to_json()
with open('ocr_training/saved_models/cnnModel.json', 'w') as json_file:
    json_file.write(cnnModel_json)
cnnModel.save_weights('ocr_training/saved_models/cnnModel.h5')
print("Model Saved")