from flask import Flask, send_file, request, jsonify
from PIL import Image, ImageDraw, ImageFont
import io
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Image Generator API</h1>
    <p>Endpoints:</p>
    <ul>
        <li>GET /generate - Generate a cute drawing image</li>
        <li>GET /generate?text=YourText - Generate image with custom text</li>
        <li>GET /generate?text=Hello&color=blue&size=800 - Customize text, color and size</li>
    </ul>
    '''

@app.route('/generate')
def generate_image():
    # Get parameters from query string
    text = request.args.get('text', 'Cute Drawing!')
    color = request.args.get('color', 'pink')
    size = int(request.args.get('size', '600'))
    
    # Create a new image
    img = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw a cute face
    face_color = color
    # Head
    draw.ellipse([size//4, size//4, 3*size//4, 3*size//4], fill=face_color, outline='black', width=3)
    
    # Eyes
    eye_y = size//2 - size//10
    draw.ellipse([size//3, eye_y, size//3 + size//15, eye_y + size//15], fill='black')
    draw.ellipse([2*size//3 - size//15, eye_y, 2*size//3, eye_y + size//15], fill='black')
    
    # Smile
    draw.arc([size//3, size//2, 2*size//3, 2*size//3], start=0, end=180, fill='black', width=3)
    
    # Add text
    try:
        # Try to use a default font
        font = ImageFont.truetype("arial.ttf", size//20)
    except:
        font = ImageFont.load_default()
    
    # Get text bounding box for centering
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (size - text_width) // 2
    text_y = size - size//6
    
    draw.text((text_x, text_y), text, fill='black', font=font)
    
    # Save to bytes
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
