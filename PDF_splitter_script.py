from PyPDF2 import PdfReader, PdfWriter # type: ignore
import os

pdf_list = [file for file in os.listdir() if '.pdf' in file]

for file_name in pdf_list:

    reader = PdfReader(file_name)

    pages = (0,len(reader.pages))

    for page_num, page in enumerate(reader.pages, 1):
        writer = PdfWriter()
        writer.add_page(page)
        new_file_name = file_name.removesuffix('.pdf')
        single_page = open(f'{new_file_name}p{page_num}.pdf', 'wb')
        writer.write(single_page)
        single_page.close()
        writer.close()