#TESTING
import os
from tabula import read_pdf

pdf_file = r"PDF file path .pdf"
df = read_pdf(pdf_file, pages='all', multiple_tables=True)

if not os.path.exists(os.path.splitext(pdf_file.split("/")[4])[0]):
    os.mkdir(os.path.splitext(pdf_file.split("/")[4])[0])
save_path = os.path.splitext(pdf_file.split("/")[4])[0] + '/'
i = 1
for data in df:
    data.to_excel(save_path+"table_"+str(i)+".xlsx")
    i = i+1

