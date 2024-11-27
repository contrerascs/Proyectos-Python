import camelot

table = camelot.read_pdf(r'Extract-Table-PDF/foo.pdf', pages='1')
print(table)