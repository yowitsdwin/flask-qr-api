from flask import Flask, jsonify, request, send_file, render_template_string
from flask_cors import CORS
import qrcode
import io
import base64
import barcode
from barcode.writer import ImageWriter
from PIL import Image
import cv2
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Your existing API routes remain the same
@app.route('/generate-qr', methods=['POST'])
def generate_qr_post():
    data = request.json
    text = data.get("text", "Hello World")
    box_size = data.get("box_size", 8)
    border = data.get("border", 2)
    fill_color = data.get("fill_color", "black")
    back_color = data.get("back_color", "white")

    qr = qrcode.QRCode(box_size=box_size, border=border)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    img_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return jsonify({"qr_code_base64": img_b64})

@app.route('/generate-qr/png', methods=['POST'])
def generate_qr_png_post():
    data = request.json
    text = data.get("text", "Hello World")
    box_size = data.get("box_size", 8)
    border = data.get("border", 2)
    fill_color = data.get("fill_color", "black")
    back_color = data.get("back_color", "white")

    qr = qrcode.QRCode(box_size=box_size, border=border)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png', as_attachment=False, download_name="qrcode.png")

@app.route('/generate-barcode', methods=['POST'])
def generate_barcode():
    data = request.json
    text = data.get("text", "123456789012")

    try:
        barcode_format = data.get("format", "code128").lower()
        BARCODE_CLASS = barcode.get_barcode_class(barcode_format)
    except barcode.errors.BarcodeNotFoundError:
        return jsonify({"error": f"Unsupported barcode format: {barcode_format}"}), 400

    buffer = io.BytesIO()
    try:
        code = BARCODE_CLASS(text, writer=ImageWriter())
        code.write(buffer)
    except Exception as e:
        return jsonify({"error": f"Failed to generate barcode: {str(e)}"}), 500

    buffer.seek(0)
    img_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return jsonify({
        "barcode_base64": img_b64,
        "format": barcode_format,
        "mime_type": "image/png"
    })

@app.route('/generate-barcode/png', methods=['POST'])
def generate_barcode_png():
    data = request.json
    text = data.get("text", "123456789012")
    barcode_format = data.get("format", "code128").lower()

    try:
        BarcodeClass = barcode.get_barcode_class(barcode_format)
    except barcode.errors.BarcodeNotFoundError:
        return jsonify({"error": f"Unsupported barcode format: {barcode_format}"}), 400

    buffer = io.BytesIO()
    try:
        barcode_instance = BarcodeClass(text, writer=ImageWriter())
        barcode_instance.write(buffer)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    buffer.seek(0)
    return send_file(
        buffer,
        mimetype='image/png',
        as_attachment=False,
        download_name="barcode.png"
    )

def decode_image_opencv(pil_img):
    img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    detector = cv2.QRCodeDetector()

    data, points, _ = detector.detectAndDecode(img)
    if data:
        return [{"type": "QRCODE", "data": data}]
    else:
        return None

@app.route('/decode/upload', methods=['POST'])
def decode_upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
        
    try:
        img = Image.open(file.stream).convert('RGB')
    except Exception as e:
        return jsonify({"error": f"Invalid image file: {str(e)}"}), 400

    decoded = decode_image_opencv(img)
    if not decoded:
        return jsonify({"error": "No QR code detected"}), 404

    return jsonify({"decoded": decoded})

@app.route('/decode/camera', methods=['POST'])
def decode_camera():
    data = request.json
    img_b64 = data.get("image_base64")
    if not img_b64:
        return jsonify({"error": "No image_base64 provided"}), 400

    try:
        img_bytes = base64.b64decode(img_b64)
        img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
    except Exception as e:
        return jsonify({"error": f"Invalid image data: {str(e)}"}), 400

    decoded = decode_image_opencv(img)
    if not decoded:
        return jsonify({"error": "No QR code detected"}), 404

    return jsonify({"decoded": decoded})

# NEW: Serve the HTML frontend
@app.route('/')
def index():
    return render_template('./templates/index.html')

if __name__ == '__main__':
    app.run(debug=True)