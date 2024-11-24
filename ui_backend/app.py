from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# UI endpoint to upload the image
@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        file = request.files["image"]
        if not file:
            return "No file uploaded", 400
        
        # Send the image to the AI service for detection
        response = requests.post("http://ai_service:8001/detect", files={"file": file})
        data = response.json()
        
        # Pass the detections to the result template
        return render_template("result.html", detections=data["detections"])
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
