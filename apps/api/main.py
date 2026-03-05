from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import io
from PIL import Image

app = FastAPI(title="Smart Traffic AI - Inference API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

def dummy_predict(img: Image.Image):
    # TODO: replace with real model inference
    return {"label": "unknown", "confidence": 0.0}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        return JSONResponse(status_code=400, content={"error": "Upload an image file."})

    content = await file.read()
    img = Image.open(io.BytesIO(content)).convert("RGB")

    pred = dummy_predict(img)
    return {"filename": file.filename, **pred}
