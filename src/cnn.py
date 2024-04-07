import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from keras.callbacks import ModelCheckpoint
from tensorflow.keras.preprocessing import image

class DeepFakeDetectionModel(tf.keras.Model):
    def __init__(self):
        super(DeepFakeDetectionModel, self).__init__()
        self.conv1 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3))
        self.maxpool1 = tf.keras.layers.MaxPooling2D(2, 2)
        self.conv2 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu')
        self.maxpool2 = tf.keras.layers.MaxPooling2D(2, 2)
        self.conv3 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu')
        self.maxpool3 = tf.keras.layers.MaxPooling2D(2, 2)
        self.conv4 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu')
        self.maxpool4 = tf.keras.layers.MaxPooling2D(2, 2)
        self.flatten = tf.keras.layers.Flatten()
        self.dropout = tf.keras.layers.Dropout(0.5)
        self.dense1 = tf.keras.layers.Dense(512, activation='relu')
        self.dense2 = tf.keras.layers.Dense(1, activation='sigmoid')

    def call(self, inputs):
        x = self.conv1(inputs)
        x = self.maxpool1(x)
        x = self.conv2(x)
        x = self.maxpool2(x)
        x = self.conv3(x)
        x = self.maxpool3(x)
        x = self.conv4(x)
        x = self.maxpool4(x)
        x = self.flatten(x)
        x = self.dropout(x)
        x = self.dense1(x)
        return self.dense2(x)

class DeepFakeDetector:
    def __init__(self):
        self.model = DeepFakeDetectionModel()
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def load_model_weights(self, filepath):
        self.model.load_weights(filepath)
        print("Model weights loaded successfully.")

    def preprocess_image(img):
        img = img.resize((256,256))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        return img_array