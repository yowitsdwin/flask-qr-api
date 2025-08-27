from flask import Flask, jsonify, request, send_file
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/generate-qr', methods=['POST'])
def generate_qr_post():
    data = request.json  # get JSON data from request body
    text = data.get("text", "Hello World")   # required field
    box_size = data.get("box_size", 8)       # optional customization
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


if __name__ == '__main__':
    app.run(debug=True)
