import io
import qrcode
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', qr_code=None)

@app.route('/generate_qr_code', methods=['POST'])
def generate_qr_code():
    selected_checkboxes = request.form.getlist('checkboxes[]')

    # Combine selected checkboxes into a single string
    selected_data = ", ".join(selected_checkboxes)

    # Generate the QR code
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(selected_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image to a bytes buffer
    buffer = io.BytesIO()
    qr_img.save(buffer, format='PNG')
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

