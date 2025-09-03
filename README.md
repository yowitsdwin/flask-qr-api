# flask-qr-api

# 🧾 QR Code Generator API

A lightweight Flask-based REST API for generating customizable QR codes. Supports returning QR codes as Base64 strings or downloadable PNG images.

Created and Developed By :
Abelgas, Junel 
Ang, Joost Laven
Casicas, James
Singson, John Rey 
Tumulak, Aldwin

## 🚀 Features

- Generate QR codes from text or URLs
- Customize QR code appearance (color, size, border)
- Return as Base64 string or PNG image
- Lightweight and fast (uses Flask + qrcode)

## 📦 Requirements

- Python 3.7+
- Flask
- qrcode

### 🔧 Installation

```bash
pip install flask qrcode[pil]

---

### 🔹 Step 5: Add How to Run the API

```markdown
## 🛠️ Running the API

```bash
python app.py

The API will start at:
http://127.0.0.1:5000/


---

### 🔹 Step 6: Document the API Endpoints

Use tables and examples to document your endpoints.

#### Example for Base64 QR Endpoint:

```markdown
### 📌 Generate QR Code as Base64

**Endpoint:**  
`POST /generate-qr`

**Request Body:**

| Field         | Type    | Required | Default        | Description                               |
|---------------|---------|----------|----------------|-------------------------------------------|
| `text`        | string  | No       | "Hello World"  | Text or URL to encode in QR code          |
| `box_size`    | int     | No       | 8              | Size of QR boxes                           |
| `border`      | int     | No       | 2              | Width of border in boxes                  |
| `fill_color`  | string  | No       | "black"        | Foreground color                          |
| `back_color`  | string  | No       | "white"        | Background color                          |

**Example Request:**

```json
{
  "text": "https://example.com",
  "fill_color": "blue",
  "back_color": "white"
}

Example Response:
{
  "qr_code_base64": "iVBORw0KGgoAAAANSUhEUgAAA..."
}

Repeat this for the `/generate-qr/png` endpoint.

---

### 🔹 Step 7: Add cURL Examples

Provide users with ready-to-copy command-line examples:

```markdown
## 🧪 Example with cURL

### Generate QR as Base64

```bash
curl -X POST http://localhost:5000/generate-qr \
  -H "Content-Type: application/json" \
  -d '{"text":"https://openai.com"}'

Download PNG Image
curl -X POST http://localhost:5000/generate-qr/png \
  -H "Content-Type: application/json" \
  -d '{"text":"https://openai.com"}' \
  --output qrcode.png

---

### 🔹 Step 8: Add Optional Sections

Add any of these if applicable:

#### 📁 Project Structure

```markdown
## 📁 Project Structure



## 🛡️ License

This project is licensed under the MIT License.

## 🤝 Contributing

Pull requests and feedback are welcome! Open an issue or submit a PR.
