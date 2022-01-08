'''
requirements: 
    pip install pyttsx3
    pip install PyPDF2
    
'''

import PyPDF2
import pyttsx3



file_name = input('enter the pdf file name(file.pdf) : ')
pdfReader = PyPDF2.PdfFileReader(open(file_name, 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()


speaker.save_to_file(text, 'audio.mp3')
speaker.runAndWait()