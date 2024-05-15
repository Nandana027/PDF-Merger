from pypdf import PdfMerger
pdfs=["stp report file-1 (1).pdf","pehla half.pdf","stp report file editted-10-35.pdf"]

merger=PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()