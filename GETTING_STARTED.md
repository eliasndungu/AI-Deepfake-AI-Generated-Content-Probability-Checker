# Getting Started Guide

Welcome to the AI-Generated Content Probability Checker! This guide will help you get up and running quickly.

## Quick Start (3 Steps)

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

### 3. Open Your Browser

Navigate to `http://localhost:5000` and start analyzing images!

## What Does This Tool Do?

This tool analyzes images to estimate the probability they were created by AI systems like:
- Midjourney
- DALL-E
- Stable Diffusion
- Other AI image generators

## How to Use the Web Interface

1. **Upload an Image**: Click the upload area or drag and drop an image file
2. **Click Analyze**: Press the "Analyze Image" button
3. **Review Results**: See your probability score and contributing factors

### Understanding Results

- **Probability Score**: 0-100% indicating likelihood of AI generation
- **Confidence Level**: 
  - **High**: Analysis factors agree strongly
  - **Medium**: Moderate agreement between factors
  - **Low**: Analysis factors show conflicting signals
  
- **Contributing Factors**:
  - **EXIF Analysis**: Checks metadata patterns
  - **Compression Artifacts**: Examines compression patterns
  - **Color Distribution**: Analyzes color channel characteristics
  - **Statistical Patterns**: Evaluates image dimensions and properties

## Using the API

### Health Check

```bash
curl http://localhost:5000/api/health
```

Response:
```json
{
  "status": "healthy",
  "service": "AI Content Detection API",
  "version": "1.0.0"
}
```

### Analyze an Image

```bash
curl -X POST -F "image=@path/to/your/image.jpg" http://localhost:5000/api/analyze
```

Response:
```json
{
  "success": true,
  "probability": 0.652,
  "confidence": "medium",
  "factors": {
    "exif_analysis": 0.7,
    "compression_artifacts": 0.5,
    "color_distribution": 0.7,
    "statistical_patterns": 0.6
  },
  "disclaimer": "This analysis provides an estimate..."
}
```

### Python Example

```python
import requests

url = "http://localhost:5000/api/analyze"
files = {"image": open("image.jpg", "rb")}

response = requests.post(url, files=files)
result = response.json()

print(f"Probability: {result['probability'] * 100}%")
print(f"Confidence: {result['confidence']}")
```

## Supported Image Formats

- PNG (.png)
- JPEG (.jpg, .jpeg)
- GIF (.gif)
- BMP (.bmp)

**Maximum file size**: 16MB

## Important Disclaimer

⚠️ **This tool provides estimates, not definitive proof**

- Results should be used as guidance only
- False positives and false negatives can occur
- AI detection technology is continuously evolving
- Do not use for political labeling or claims of absolute truth

## Troubleshooting

### Common Issues

**Issue**: "Module not found" error
**Solution**: Make sure you've installed dependencies: `pip install -r requirements.txt`

**Issue**: Port 5000 already in use
**Solution**: Change the port in `app.py` or stop the other application using port 5000

**Issue**: "File too large" error
**Solution**: Reduce your image size to under 16MB

**Issue**: Analysis taking too long
**Solution**: Try a smaller image resolution

## Development Mode

To enable debug mode for development:

```bash
FLASK_DEBUG=true python app.py
```

**Warning**: Never use debug mode in production!

## Production Deployment

For production use, deploy with a production WSGI server:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

Or use other production servers like:
- uWSGI
- mod_wsgi
- waitress

## Need Help?

- Check the [README.md](README.md) for detailed documentation
- Review the code comments in `detector.py` for technical details
- Check the Flask logs for error messages

## Contributing

Found a bug or have a feature suggestion? Please:
1. Check existing issues
2. Create a detailed issue report
3. Consider submitting a pull request

## License

This project is provided as-is for educational and research purposes.
