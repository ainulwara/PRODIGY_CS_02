from PIL import Image

def encrypt_image(input_path, output_path, key):
    # Open the input image
    image = Image.open(input_path)
    # Convert the image to RGB mode (if not already)
    image = image.convert("RGB")
    # Get the pixel data
    pixels = list(image.getdata())
    # Encrypt the pixels using XOR
    encrypted_pixels = [(r ^ key, g ^ key, b ^ key) for r, g, b in pixels]
    # Create a new image with the encrypted pixels
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    # Save the encrypted image
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(input_path)
    # Convert the image to RGB mode (if not already)
    encrypted_image = encrypted_image.convert("RGB")
    # Get the pixel data
    encrypted_pixels = list(encrypted_image.getdata())
    # Decrypt the pixels using XOR
    decrypted_pixels = [(r ^ key, g ^ key, b ^ key) for r, g, b in encrypted_pixels]
    # Create a new image with the decrypted pixels
    decrypted_image = Image.new(encrypted_image.mode, encrypted_image.size)
    decrypted_image.putdata(decrypted_pixels)
    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

# Main program
if __name__ == "__main__":
    print("Choose an option:")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        input_path = input("Enter the path of the image to encrypt: ")
        output_path = input("Enter the path to save the encrypted image: ")
        key = int(input("Enter the encryption key (an integer): "))
        encrypt_image(input_path, output_path, key)
    elif choice == "2":
        input_path = input("Enter the path of the encrypted image: ")
        output_path = input("Enter the path to save the decrypted image: ")
        key = int(input("Enter the decryption key (same as encryption key): "))
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice. Exiting.")
