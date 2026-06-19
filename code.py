"""
Biox Systems QR Code Generator
------------------------------
A professional script to generate QR codes from URL inputs.
Follows coding best practices and PEP 8 standards.
"""

import qrcode
import sys

def create_biox_qr(url_data, output_name="biox_qr_output.png"):
    """
    Encodes a URL into a QR code and saves it as a PNG file.
    
    Args:
        url_data (str): The URL to be encoded.
        output_name (str): The filename for the generated image.
    """
    try:
        # Initialize QR Code configuration
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

        # Add data to the instance
        qr.add_data(url_data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        # Using standard black on white for maximum scannability
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image file
        img.save(output_name)
        
        print(f"\n[+] Success! QR Code generated for: {url_data}")
        print(f"[+] File saved as: {output_name}")

    except Exception as error:
        print(f"\n[!] An error occurred during generation: {error}")

def main():
    """
    Main entry point for the application.
    Handles user input and basic validation.
    """
    print("========================================")
    print("      BIOX SYSTEMS QR GENERATOR        ")
    print("========================================\n")
    
    # Get URL from user
    target_url = input("Enter the URL to generate a QR code: ").strip()
    
    if not target_url:
        print("[!] Error: URL input cannot be empty.")
        return

    # Generate the QR code
    create_biox_qr(target_url)

if __name__ == "__main__":
    main()