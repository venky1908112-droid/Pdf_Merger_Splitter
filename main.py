from pypdf import PdfReader, PdfWriter


def merge_pdfs():

    pdf1 = input("Enter First PDF Name: ")
    pdf2 = input("Enter Second PDF Name: ")

    writer = PdfWriter()

    for pdf_file in [pdf1, pdf2]:

        reader = PdfReader(pdf_file)

        for page in reader.pages:
            writer.add_page(page)

    with open("merged.pdf", "wb") as file:
        writer.write(file)

    print("PDFs Merged Successfully!")


from pypdf import PdfReader, PdfWriter

from pypdf import PdfReader, PdfWriter

def split_pdf():

    pdf_file = input("Enter PDF Name: ")

    reader = PdfReader(pdf_file)

    total_pages = len(reader.pages)

    middle = total_pages // 2

    first_half = PdfWriter()
    second_half = PdfWriter()

    for i in range(middle):
        first_half.add_page(reader.pages[i])

    for i in range(middle, total_pages):
        second_half.add_page(reader.pages[i])

    with open("first_half.pdf", "wb") as file:
        first_half.write(file)

    with open("second_half.pdf", "wb") as file:
        second_half.write(file)

    print("PDF Split Successfully!")


while True:

    print("\n===== PDF Tool =====")
    print("1. Merge PDFs")
    print("2. Split PDF")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        merge_pdfs()

    elif choice == "2":
        split_pdf()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")