# AI-Generated Content Probability Checker

A web-based tool that analyzes images to estimate the probability they were created by AI systems. This MVP focuses on image-based detection using statistical analysis and heuristic approaches.

## Features

- **Image Upload**: Support for PNG, JPG, JPEG, GIF, and BMP formats
- **Probability Scoring**: Returns a 0-100% probability score indicating likelihood of AI generation
- **Multi-Factor Analysis**: Analyzes multiple characteristics including:
  - EXIF metadata patterns
  - Compression artifacts
  - Color distribution
  - Statistical patterns
- **Confidence Levels**: Provides high/medium/low confidence ratings
- **User-Friendly Interface**: Clean, modern web UI with drag-and-drop support
- **API Endpoint**: RESTful API for programmatic access

## Important Disclaimer

⚠️ **This tool provides estimates based on technical characteristics and should not be considered definitive proof.** AI detection technology is continuously evolving, and this tool may produce false positives or false negatives. Use results as guidance only, not as absolute truth. This tool does not make claims about content authenticity or truth, and is not intended for political labeling.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/eliasndungu/AI-Deepfake-AI-Generated-Content-Probability-Checker.git
cd AI-Deepfake-AI-Generated-Content-Probability-Checker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Web Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Upload an image using the web interface and click "Analyze Image"

### API Usage

The application provides a REST API endpoint for programmatic access:

**Endpoint**: `POST /api/analyze`

**Request**: Multipart form data with an `image` field

**Example using curl**:
```bash
curl -X POST -F "image=@path/to/image.jpg" http://localhost:5000/api/analyze
```

**Example Response**:
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
  "disclaimer": "This analysis provides an estimate based on technical characteristics..."
}
```

**Health Check Endpoint**: `GET /api/health`

```bash
curl http://localhost:5000/api/health
```

## How It Works

The detector uses multiple heuristic approaches to analyze images:

1. **EXIF Metadata Analysis**: Checks for camera information, software tags, and metadata patterns typical of AI-generated images

2. **Compression Artifact Analysis**: Examines local variance patterns that may indicate AI smoothing or unusual compression

3. **Color Distribution Analysis**: Analyzes color channel statistics and correlations that are characteristic of AI-generated content

4. **Statistical Pattern Analysis**: Checks image dimensions and other statistical properties common in AI-generated images

Each factor contributes to a weighted final probability score. The confidence level is determined by how well the different factors agree with each other.

## Supported Image Formats

- PNG (.png)
- JPEG (.jpg, .jpeg)
- GIF (.gif)
- BMP (.bmp)

Maximum file size: 16MB

## Project Structure

```
.
├── app.py              # Flask web application
├── detector.py         # Core detection logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Web UI
└── README.md          # This file
```

## Limitations

- **MVP Implementation**: This is a minimum viable product using heuristic approaches. For production use, consider integrating trained machine learning models.
- **Image Analysis Only**: Currently supports only images; video and audio analysis are not included in this MVP.
- **Not Definitive**: Results should be used as guidance, not proof of AI generation.
- **Evolving AI Technology**: As AI generation technology improves, detection methods must also evolve.

## Future Enhancements

Potential improvements for future versions:

- Integration with trained ML models for improved accuracy
- Support for video and audio analysis
- Batch processing capabilities
- Advanced deep learning-based detection
- Integration with external AI detection APIs
- Database storage for analysis history
- User authentication and rate limiting

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is provided as-is for educational and research purposes.

## Ethical Considerations

This tool is designed to help identify AI-generated content for transparency and awareness purposes. It should not be used to:
- Make definitive claims about content authenticity
- Politically label or categorize content
- Harm individuals or organizations
- Circumvent content policies without proper context

Always use this tool responsibly and in conjunction with other verification methods.