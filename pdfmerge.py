from pypdf import PdfWriter
import glob
from natsort import natsorted

pdfs = glob.glob('*.pdf')
pdfs = natsorted(pdfs)


merger = PdfWriter()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()