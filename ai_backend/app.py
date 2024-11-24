from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import torch
from PIL import Image
import io
import uvicorn

app = FastAPI()

# Load the YOLOv5 model during startup
try:
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, force_reload=True, trust_repo=True)
except Exception as e:
    raise RuntimeError(f"Error loading YOLOv5 model: {str(e)}")


@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    # Ensure the file is an image
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file is not an image")

    try:
        # Read the uploaded file and convert to a PIL Image
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data)).convert("RGB")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing image: {str(e)}")

    # Perform object detection using YOLOv5
    try:
        results = model(image)
        detections = results.pandas().xyxy[0].to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during detection: {str(e)}")

    # Return detection results as JSON
    return JSONResponse(content={"detections": detections})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
