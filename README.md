# Flask-API

## 🧾 QR Code and Barcode Generator API

A lightweight Flask-based REST API for generating customizable QR codes and barcodes.  
Supports returning images as Base64 strings or downloadable PNG files.  
Also supports decoding QR codes and barcodes from uploaded images or base64 data.

---

### Created and Developed By:  
- Abelgas, Junel  
- Ang, Joost Laven  
- Casicas, James  
- Singson, John Rey  
- Tumulak, Aldwin  

BSIT3-1 SIA  
SIA instructor: Mr. Yestin Roy A. Prado

---

## 🚀 Features

- Generate QR codes and barcodes from text or URLs  
- Customize QR code appearance (color, size, border)  
- Return QR/barcode as Base64 string or PNG image  
- Decode QR codes and barcodes from uploaded images or base64-encoded camera captures  
- Lightweight and fast (built with Flask + qrcode + python-barcode + pyzbar)

---

## 📦 Requirements

- Python 3.7+  
- Flask  
- qrcode[pil]  
- Pillow  
- python-barcode  
- pyzbar  
- gunicorn (optional, for production)

---

## 🔧 Installation

```bash
pip install -r requirements.txt


```
## 🛠️ Running the API

```bash
python app.py
```

The API will start at:

```bash
http://127.0.0.1:5000/
```

## 📁 Project Structure

```bash
flask-qr-api/
│
├── app.py           # Flask application with all endpoints
├── requirements.txt # Dependencies list
└── README.md        # This documentation

```

## 📌 API Endpoints
1. Generate QR Code as Base64

POST /generate-qr

Request Body:

```bash
Field	Type	Required	Default	Description
text	string	No	"Hello World"	Text or URL to encode
box_size	int	No	8	Size of QR code boxes
border	int	No	2	Border width
fill_color	string	No	"black"	Foreground color
back_color	string	No	"white"	Background color
```

Example Request:
```bash
{
  "text": "https://example.com",
  "fill_color": "blue",
  "back_color": "white"
}
```

Example Response:
```bash
{
  "qr_code_base64": "iVBORw0KGgoAAAANSUhEUgAAA..."
}
```
2. Generate QR Code as PNG Image

POST /generate-qr/png

Same request body as above.

Returns: PNG image file.
3. Generate Barcode as Base64

POST /generate-barcode

Request Body:

Field	Type	Required	Default	Description
text	string	No	"123456789012"	Text to encode in barcode
format	string	No	"code128"	Barcode format (e.g., code128, ean13)

Example Request:
```bash
{
  "text": "012345678905",
  "format": "ean13"
}
```

Example Response:
```bash
{
  "barcode_base64": "iVBORw0KGgoAAAANSUhEUgAAA...",
  "format": "ean13",
  "mime_type": "image/png"
}
```
4. Generate Barcode as PNG Image

POST /generate-barcode/png

Same request body as above. Returns PNG image file.

5. Decode QR/Barcode from Uploaded Image

POST /decode/upload

Form Data:

file: Image file to upload (QR code or barcode)

Example Response:
```bash
{
  "decoded": [
    {
      "type": "QRCODE",
      "data": "https://example.com"
    }
  ]
}
```
6. Decode QR/Barcode from Base64 Image

POST /decode/camera

Request Body:

Field	Type	Required	Description
image_base64	string	Yes	Base64-encoded image data

Example Request:
```bash
{
  "image_base64": "<base64-encoded-image-string>"
}
```
## 🧪 Example cURL Requests
Generate QR as Base64
```bash
curl -X POST http://localhost:5000/generate-qr \
  -H "Content-Type: application/json" \
  -d '{"text":"https://openai.com"}'
```

Download QR as PNG Image
```bash
curl -X POST http://localhost:5000/generate-qr/png \
  -H "Content-Type: application/json" \
  -d '{"text":"https://openai.com"}' \
  --output qrcode.png
```

Generate Barcode as Base64
```bash
curl -X POST http://localhost:5000/generate-barcode \
  -H "Content-Type: application/json" \
  -d '{"text":"012345678905","format":"ean13"}'
```

Download Barcode as PNG Image
```bash
curl -X POST http://localhost:5000/generate-barcode/png \
  -H "Content-Type: application/json" \
  -d '{"text":"012345678905","format":"ean13"}' \
  --output barcode.png
```

Decode QR/Barcode from Uploaded Image
```bash
curl -X POST http://localhost:5000/decode/upload \
  -F "file=@/path/to/your/image.png"
```

Decode QR/Barcode from Base64 Image
```bash
curl -X POST http://localhost:5000/decode/camera \
  -H "Content-Type: application/json" \
  -d '{"image_base64":"<base64-string>"}'
```
