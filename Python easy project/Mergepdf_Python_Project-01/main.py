# Code Start here....
from PyPDF2 import PdfMerger #import module
ourfiles=["Pdf.pdf","Pdf2.pdf"] # Our pdf files
margefile=PdfMerger()
for bothfile in ourfiles: # Loop files
    margefile.append(bothfile)
margefile.write("New.pdf") # Wrire new Pdf
margefile.close() # Closing