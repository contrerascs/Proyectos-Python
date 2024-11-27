import camelot

table = camelot.read_pdf(r'Extract-Table-PDF/foo.pdf', pages='1')
print(table)

table.export(r'Extract-Table-PDF/foo.csv',f='csv', compress=True)
table[0].to_csv(r'Extract-Table-PDF/foo.csv')