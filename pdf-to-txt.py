import pdftotext

with open("gender_trouble.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

with open('gender_trouble.txt', 'w') as f:
    f.write("\n\n".join(pdf))
 