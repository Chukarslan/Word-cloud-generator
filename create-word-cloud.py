import os
import PyPDF2
from wordcloud import WordCloud
import matplotlib.pyplot as plt

pdf_files = [file for file in os.listdir() if file.endswith('.pdf')]

text = ""

for file in pdf_files:
    with open(file, 'rb') as pdf:
        pdf_reader = PyPDF2.PdfFileReader(pdf)
        for page in range(pdf_reader.numPages):
            text += pdf_reader.getPage(page).extractText()

wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
