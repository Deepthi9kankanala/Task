import fitz

file = 'AddImage.pdf'
pdf = fitz.open(file)
img_list = pdf.get_page_images(0)  # Get images from the first page
for img_index, img in enumerate(img_list):
    xref = img[0]  # Image reference
    pix = fitz.Pixmap(pdf, xref)  # Get pixmap for the image
    if pix.n < 5:
        pix.writePNG(f'{xref}.png')  # Write PNG image
    else:
        pix1 = fitz.Pixmap(fitz.csRGB, pix)
        pix1.writePNG(f'{xref}.png')
        pix1 = None
    pix = None
print(len(img_list), 'images detected')
