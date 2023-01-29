from fpdf import FPDF
import random
import string

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font("Arial", "B", 15)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, 1, 1, "C", True)
        # Line break
        self.ln(10)
        
    def footer(self):
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Select Arial italic 8
        self.set_font("Arial", "I", 8)
        # Page number
        self.cell(0, 10, "Page %s" % self.page_no(), 0, 0, "C")

pdf = PDF()
title = "Trashy Text Report"
pdf.set_title(title)
for i in range(3):
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for j in range(20):
        pdf.cell(0, 10, random_string(20), 0, 1)
pdf.output("trashy_text.pdf", "F")
