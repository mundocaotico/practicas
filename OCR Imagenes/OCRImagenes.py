
# IMPORTS

from PIL import Image
import os
import pytesseract
from fpdf import FPDF

##########

pdf = FPDF()

ruta_imagenes = os.getcwd()+'\\ruta_imagenes'
#print(ruta_imagenes)
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
i = 0
img = []
abrir_imagenes = ''
convertir_a_texto = ''
os.chdir(ruta_imagenes)

#BUCLE AÑADIR IMAGENES AL ARRAY
archivos_directorio = os.listdir()
for file in archivos_directorio:
    img.append(file)

###############################

# Abrir imagenes y convertir a texto
contador_array = len(img) - 1
print(contador_array)
while i <= contador_array:
    try:
        abrir_imagenes = Image.open(img[i])
        convertir_a_texto = pytesseract.image_to_string(img[i], lang='eng')
        convertir_a_latin1 = convertir_a_texto.encode('latin-1', 'ignore').decode('latin-1')
        pdf.add_page()
        pdf.set_font('Arial', size = 13)
        #pdf.cell(200,10,txt = convertir_a_latin1, align = 'C')
        pdf.multi_cell(200, 10, txt = convertir_a_latin1, border = 0,
        align = 'C')
        print(img[i])
        i+= 1
    except:
        print('Ha ocurrido un error. Compruebe el directorio de las imagenes')
        break
    
#os.chdir('..\\')
pdf.output('..\\test.pdf')

############################################

# PRUEBAS CON PRINT

#print(pytesseract.get_languages())
#print(convertir_a_texto)