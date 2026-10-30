# Image Generator Service

Oru simple image generation service - Render.com la deploy panna.

## Features
- Cute drawing images generate pannum
- Custom text, color, size options
- REST API endpoints

## Render la deploy pannradhu eppadi:

1. **GitHub repository create pannunga:**
   - GitHub la new repo create pannunga
   - Indha files ellam antha repo la push pannunga:
     - app.py
     - requirements.txt
     - render.yaml

2. **Render.com la deploy pannunga:**
   - https://render.com la sign up pannunga (GitHub account use pannalam)
   - "New +" button click pannunga
   - "Web Service" select pannunga
   - Unga GitHub repo connect pannunga
   - Render automatically detect panniduvanga Python app-a
   - "Create Web Service" click pannunga

3. **Deploy aagum:**
   - 2-3 minutes la deploy aagum
   - Ungalukku oru URL kidaikum: `https://your-service.onrender.com`

## API Usage:

### Basic image:
```
https://your-service.onrender.com/generate
```

### Custom text:
```
https://your-service.onrender.com/generate?text=Hello
```

### Custom color and size:
```
https://your-service.onrender.com/generate?text=Welcome&color=lightblue&size=800
```

## Parameters:
- `text` - Image la irukka text (default: "Cute Drawing!")
- `color` - Face color (default: "pink") - any CSS color name
- `size` - Image size in pixels (default: 600)

## Colors neenga use pannalam:
- pink, lightblue, lightgreen, yellow, orange, lavender, peachpuff, etc.

## Local la test pannunga:

```bash
pip install -r requirements.txt
python app.py
```

Apram browser la: http://localhost:5000
