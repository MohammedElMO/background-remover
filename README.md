# Background Remover

A simple yet powerful web application that allows users to upload images and remove backgrounds with a single click. Built with Streamlit and the Rembg library.

![Background Remover Demo](https://github.com/MohammedElMO/background-remover/raw/main/demo.png)

## Features

- Clean and intuitive user interface
- Support for common image formats (JPG, JPEG, PNG)
- One-click background removal
- Side-by-side comparison of original and processed images
- Download functionality for processed images
- Error handling for invalid uploads
- Responsive layout that works on different screen sizes

## Requirements

- Python 3.8 or higher
- Dependencies listed in `requirements.txt`:
  - streamlit>=1.20.0
  - rembg>=2.0.0
  - Pillow>=9.0.0

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/MohammedElMO/background-remover.git
   cd background-remover
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. After installation, run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL displayed in your terminal (typically http://localhost:8501).

3. Upload an image using the file uploader.

4. Click the "Remove Background" button to process the image.

5. Once processing is complete, you can download the processed image with the transparent background.

## How It Works

The application uses the [Rembg](https://github.com/danielgatis/rembg) library, which is built on deep learning models to detect and remove backgrounds from images. The Streamlit framework provides the web interface for a seamless user experience.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributors

- [Mohammed El Amrani](https://github.com/MohammedElMO)

## Acknowledgements

- [Rembg](https://github.com/danielgatis/rembg) for the background removal technology
- [Streamlit](https://streamlit.io/) for the web application framework

