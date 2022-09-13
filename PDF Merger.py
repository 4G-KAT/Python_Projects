from PyPDF2 import PdfMerger
import os

path = str(input("Enter the folder path: ").strip())

os.chdir(path)
pdfs = os.listdir(path)

merger = PdfMerger()

for pdf in pdfs:
    pages = tuple(input(f"Enter a page range for {pdf} : "))
    if pages:
        merger.append(fileobj=pdf, pages=(int(pages[0]), int(pages[1])))
        continue
    merger.append(fileobj=pdf)

name = input("Enter a name for the merged PDF : ")
merger.write(f"{name}.pdf")
merger.close()