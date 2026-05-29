import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
import mlflow

IMG_SIZE = 128
BATCH_SIZE = 8

train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train_data = train_datagen.flow_from_directory(
    '../dataset/train',
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='training'
)

val_data = train_datagen.flow_from_directory(
    '../dataset/train',
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='validation'
)

model = models.Sequential([
    layers.Input(shape=(128,128,3)),

    layers.Conv2D(16, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(32, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),

    layers.Flatten(),

    layers.Dense(64, activation='relu'),

    layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

mlflow.start_run()

history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=5
)

accuracy = history.history['accuracy'][-1]

mlflow.log_param("epochs", 5)
mlflow.log_metric("accuracy", accuracy)

model.save("vehicle_damage_model.h5")

mlflow.end_run()

print("Model Trained Successfully")