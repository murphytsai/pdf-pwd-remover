# pdf-pwd-remover
PDF Password Remover is a simple command-line tool for decrypting password-protected PDF files. It uses the PyPDF2 library to remove encryption and save the decrypted PDF as a new file.

## Installation

To use PDF Password Remover, you need to have Python and Pip installed. You can then install the required dependencies using Pipenv:

```bash
pipenv install
```

## Usage
PDF Password Remover can be used from the command line as follows:

```bash
python decrypt_pdf.py input.pdf password
```

The decrypted PDF will be saved as **input-decrypt.pdf** in the same directory.
