import PyPDF2 
# creating a pdf file object 
pdfFileObj = open('megalaya.pdf', 'rb') 
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
# printing number of pages in pdf file 
print(pdfReader.numPages)     
# creating a page object 
pageObj = pdfReader.getPage(0) 
print(pageObj.extractText())  
pdfFileObj.close() 



