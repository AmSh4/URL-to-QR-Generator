# URL-to-QR-Generator

A professional Python application that converts URLs into high-quality QR codes and exports them as PNG image files. This project provides a simple command-line interface for generating scannable QR codes with robust error handling and clean code architecture.

---

# Overview

URL-to-QR-Generator is a lightweight Python utility designed to generate QR codes from user-provided URLs. The generated QR codes are saved as image files and can be used for websites, portfolios, business cards, marketing materials, event registrations, and various digital sharing purposes.

The application utilizes the `qrcode` library along with the `Pillow` imaging library to create highly reliable and easily scannable QR codes.

---

# Features

## Core Functionality

* Generate QR codes from any valid URL
* Save QR codes as PNG image files
* High error correction capability
* Command-line interface for easy usage
* Automatic image generation and storage

## Code Quality

* Modular design
* PEP 8 compliant code structure
* Exception handling
* Function-based architecture
* Comprehensive documentation

## QR Code Configuration

* Error Correction Level: High (H)
* Automatic data fitting
* Optimized border spacing
* Standard black-and-white design for maximum compatibility

---

# Project Structure

```text
URL-to-QR-Generator/
│
├── code.py
├── requirements.txt
└── README.md
```

### File Descriptions

| File                 | Description                  |
| -------------------- | ---------------------------- |
| `code.py`            | Main application script      |
| `requirements.txt`   | Required Python dependencies |
| `README.md`          | Project documentation        |

---

# Requirements

## Software Requirements

* Python 3.10 or higher
* Pip package manager

## Supported Platforms

* Windows
* Linux
* macOS

---

# Installation

## Step 1: Clone the Repository

```bash
git clone https://github.com/AmSh4/URL-to-QR-Generator.git
```

## Step 2: Navigate to the Project Directory

```bash
cd URL-to-QR-Generator
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

Run the application using:

```bash
python code.py
```

You will see:

```text
========================================
      BIOX SYSTEMS QR GENERATOR
========================================
```

Enter the URL when prompted:

```text
Enter the URL to generate a QR code:
```

Example:

```text
Enter the URL to generate a QR code:
https://www.google.com
```

Upon successful generation:

```text
[+] Success! QR Code generated for: https://www.google.com
[+] File saved as: biox_qr_output.png
```

---

# How It Works

The workflow consists of the following steps:

## 1. User Input

The user enters a URL through the command line.

```python
target_url = input("Enter the URL to generate a QR code: ").strip()
```

## 2. QR Code Initialization

A QRCode object is created with predefined settings.

```python
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
```

## 3. Data Encoding

The provided URL is encoded into the QR code.

```python
qr.add_data(url_data)
```

## 4. Image Generation

The QR code is rendered into an image.

```python
img = qr.make_image(
    fill_color="black",
    back_color="white"
)
```

## 5. Export

The image is saved as a PNG file.

```python
img.save(output_name)
```

---

# Configuration

The QR code generator currently uses the following settings:

| Parameter        | Value    |
| ---------------- | -------- |
| Version          | 1        |
| Error Correction | H (High) |
| Box Size         | 10       |
| Border           | 4        |
| Foreground Color | Black    |
| Background Color | White    |

---

# Example Output

Input URL:

```text
https://github.com
```

Generated File:

```text
biox_qr_output.png
```

The generated QR code can be scanned using:

* Smartphone camera
* QR scanning applications
* Mobile payment applications
* Web-based QR scanners

---

# Dependencies

The project relies on the following Python packages:

## qrcode

Used for QR code generation.

```text
qrcode[pil]==8.0
```

## Pillow

Used for image processing and image file generation.

```text
Pillow==10.2.0
```

Install manually:

```bash
pip install qrcode[pil]
pip install Pillow
```

---

# Error Handling

The application includes exception handling mechanisms to manage unexpected failures.

Examples include:

* Empty URL input
* Invalid user input
* File generation errors
* Image saving issues
* Library-related exceptions

Example:

```python
except Exception as error:
    print(f"An error occurred during generation: {error}")
```

---

# Future Enhancements

Potential future improvements include:

* GUI-based interface using Tkinter
* Batch QR code generation
* Custom QR code colors
* Logo embedding support
* SVG export functionality
* QR code decoding functionality
* URL validation before generation
* Web-based deployment using Flask
* Downloadable QR code API

---

# Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---



