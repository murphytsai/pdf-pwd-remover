import argparse
import os
from PyPDF2 import PdfReader, PdfWriter


def decrypt_pdf(input_path, password):
    # Generate the output filename by appending "-decrypt" to the input filename
    base_name, extension = os.path.splitext(input_path)
    output_path = f"{base_name}-decrypt{extension}"

    with open(input_path, "rb") as input_file, open(output_path, "wb") as output_file:
        reader = PdfReader(input_file)
        reader.decrypt(password)

        writer = PdfWriter()

        for i in range(len(reader.pages)):
            writer.add_page(reader.pages[i])

        writer.write(output_file)

    return output_path


def main():
    parser = argparse.ArgumentParser(description="Decrypt a PDF file with a password.")
    parser.add_argument("input_filepath", help="Path to the input PDF file")
    parser.add_argument("password", help="Password for PDF decryption")

    args = parser.parse_args()

    try:
        output_filepath = decrypt_pdf(args.input_filepath, args.password)
        print(f"Decrypted PDF saved as: {output_filepath}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
