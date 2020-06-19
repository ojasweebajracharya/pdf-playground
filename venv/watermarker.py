import PyPDF2
import sys

fileToMark = sys.argv[1]
watermarkFile = sys.argv[2]

# Creates file reader:
template = PyPDF2.PdfFileReader(open(fileToMark,"rb"))
watermark = PyPDF2.PdfFileReader(open(watermarkFile,"rb"))

output = PyPDF2 = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open("watermarked_output.pdf","wb") as file:
        output.write(file)