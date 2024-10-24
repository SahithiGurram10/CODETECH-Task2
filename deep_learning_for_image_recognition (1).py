# -*- coding: utf-8 -*-
"""Deep Learning for Image Recognition.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VwX-xZJpghzuFfcqdywYvxOO5dc66EQf

DEEP LEARNING FOR IMAGE RECOGNITION

Step 1: Import Libraries
"""

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

"""Step 2: Load CIFAR-10 Dataset"""

(X_train, y_train), (X_test, y_test) = datasets.cifar10.load_data()

"""# Normalize pixel values between 0 and 1"""

X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

"""Step 3: Data Augmentation"""

datagen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True
)
datagen.fit(X_train)

"""Step 4: Build CNN Model"""

model = models.Sequential()

"""Convolutional Layer 1"""

model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))

"""Convolutional Layer 2"""

model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

"""Convolutional Layer 3"""

model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

"""Fully Connected Layers"""

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(10, activation='softmax'))

"""Step 5: Compile the Model"""

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

"""Step 6: Train the Model"""

history = model.fit(datagen.flow(X_train, y_train, batch_size=64),
                    epochs=10,
                    validation_data=(X_test, y_test))

"""Step 7: Evaluate the Model"""

test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print(f"Test Accuracy: {test_acc * 100:.2f}%")

"""
Step 8: Visualize Training Results"""

plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()

"""**Conclusion**

In conclusion, deep learning, specifically CNNs, has revolutionized the field of image recognition, enabling machines to surpass human-level performance in certain visual tasks. By employing techniques such as transfer learning, data augmentation, and advanced architectures, image recognition models have found widespread use in industries like healthcare, security, and autonomous vehicles.







"""