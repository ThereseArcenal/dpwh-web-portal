from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qr')
def qr_page():
    """Display the QR code page"""
    return render_template('qr_display.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)