from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
from PIL import Image
import numpy as np
import io

app = FastAPI()

model = tf.keras.models.load_model("../model/vehicle_damage_model.h5")

IMG_SIZE = 128

@app.get("/")
def home():
    return {"message": "Vehicle Damage Detection API Running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image_bytes = await file.read()

    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    image = image.resize((IMG_SIZE, IMG_SIZE))

    image_array = np.array(image) / 255.0

    image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array)

    result = "Whole" if prediction[0][0] > 0.5 else "Damaged"
    
    confidence = float(prediction[0][0])

    return {
        "prediction": result,
        "confidence": confidence
    }