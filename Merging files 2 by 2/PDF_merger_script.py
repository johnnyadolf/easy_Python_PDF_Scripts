from PyPDF2 import PdfReader, PdfWriter # type: ignore
import os

pdf_list = [file for file in os.listdir() if '.pdf' in file]

all_pages = []
for file_name in pdf_list:
    reader = PdfReader(file_name)
    for page in reader.pages:
        all_pages.append(page)

    # 2 by 2

    # for i, page in enumerate(all_pages, 1):
    #     if i % 2 == 1:
    #         writer = PdfWriter()
    #         writer.add_page(page)
    #         if i < len(all_pages):
    #             writer.add_page(all_pages[i])

    #         with open(f'merged_p{i}_to_p{i+1}.pdf', 'wb') as f_out:
    #             writer.write(f_out)

    #         writer.close()

    # All in one

    writer = PdfWriter()

    for page in all_pages:
        writer.add_page(page)

    with open(f'merged.pdf', 'wb') as f_out:
        writer.write(f_out)

    writer.close()