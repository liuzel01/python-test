from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass


def encrypt_pdf(origin_pdf, password, target_pdf):
    """
    It takes a PDF file, encrypts it with a password, and saves it as a new PDF file
    :param origin_pdf: the path to the original PDF file
    :param password: The password to encrypt the PDF with
    :param target_pdf: The path to the encrypted PDF file
    """
    pdfwriter = PdfFileWriter()
    pdf = PdfFileReader(origin_pdf)
    for page_num in range(pdf.numPages):
        pdfwriter.addPage(pdf.getPage(page_num))
    pdfwriter.encrypt(password)
    with open(target_pdf, "wb") as f:
        pdfwriter.write(f)
    print("done.")


if __name__ == "__main__":
    origin_pdf = "/Users/aaron/Documents/Python自动化办公.pdf"
    target_pdf = "/Users/aaron/Documents/Python自动化办公_加密.pdf"
    password = getpass.getpass(prompt="Enter password to encrypt pdf：")
    encrypt_pdf(origin_pdf, password, target_pdf)
