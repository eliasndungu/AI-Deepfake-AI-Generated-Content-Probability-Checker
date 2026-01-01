#!/usr/bin/env python3
"""
Example script demonstrating how to use the AI Content Detector
"""

from PIL import Image
import numpy as np
from detector import ImageDetector


def create_sample_image(filename='sample_test.png'):
    """Create a sample test image."""
    # Create a colorful gradient image
    width, height = 512, 512
    img_array = np.zeros((height, width, 3), dtype=np.uint8)
    
    for i in range(height):
        for j in range(width):
            img_array[i, j, 0] = int((i / height) * 255)  # Red gradient
            img_array[i, j, 1] = int((j / width) * 255)   # Green gradient
            img_array[i, j, 2] = 128                       # Blue constant
    
    image = Image.fromarray(img_array)
    image.save(filename)
    print(f"✓ Created sample image: {filename}")
    return image


def analyze_image(image_path):
    """Analyze an image file."""
    detector = ImageDetector()
    
    # Load and analyze the image
    image = Image.open(image_path)
    result = detector.analyze_image(image)
    
    # Display results
    print(f"\n{'='*60}")
    print(f"Analysis Results for: {image_path}")
    print(f"{'='*60}")
    print(f"\nAI Generation Probability: {result['probability'] * 100:.1f}%")
    print(f"Confidence Level: {result['confidence'].upper()}")
    
    print(f"\nContributing Factors:")
    for factor, value in result['factors'].items():
        bar_length = int(value * 40)
        bar = '█' * bar_length + '░' * (40 - bar_length)
        factor_name = factor.replace('_', ' ').title()
        print(f"  {factor_name:25s} [{bar}] {value * 100:5.1f}%")
    
    print(f"\n⚠️  Disclaimer:")
    print(f"  {result['disclaimer']}")
    print(f"{'='*60}\n")


def main():
    """Main function to demonstrate the detector."""
    print("\n🔍 AI-Generated Content Detector - Example Script\n")
    
    # Example 1: Create and analyze a sample image
    print("Example 1: Analyzing a generated test image")
    print("-" * 60)
    sample_image = create_sample_image('sample_test.png')
    analyze_image('sample_test.png')
    
    # Example 2: Direct analysis without saving
    print("\nExample 2: Direct image analysis")
    print("-" * 60)
    detector = ImageDetector()
    
    # Create a simple red square
    red_square = np.zeros((256, 256, 3), dtype=np.uint8)
    red_square[:, :, 0] = 255  # Red channel only
    test_img = Image.fromarray(red_square)
    
    result = detector.analyze_image(test_img)
    print(f"Red square probability: {result['probability'] * 100:.1f}%")
    print(f"Confidence: {result['confidence']}")
    
    # Example 3: Analyze your own image
    print("\n" + "="*60)
    print("To analyze your own image:")
    print("="*60)
    print("\nOption A - Using this script:")
    print("  from example import analyze_image")
    print("  analyze_image('path/to/your/image.jpg')")
    print("\nOption B - Using the web interface:")
    print("  1. Run: python app.py")
    print("  2. Open: http://localhost:5000")
    print("  3. Upload your image")
    print("\nOption C - Using the API:")
    print("  curl -X POST -F 'image=@your_image.jpg' http://localhost:5000/api/analyze")
    print()


if __name__ == '__main__':
    main()
