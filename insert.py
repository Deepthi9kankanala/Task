import fitz

def replace_text_in_pdf(input_pdf_path, output_pdf_path, old_text, new_text):
    # Open the input PDF file
    pdf_document = fitz.open(input_pdf_path)

    # Iterate through each page of the PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)

        # Search for the old text and replace it with the new text
        text_instances = page.search_for(old_text)
        for inst in text_instances:
            page.insert_text(inst[:2], new_text)

    # Save the modified PDF to a new file
    pdf_document.save(output_pdf_path)
    pdf_document.close()

# Example usage:
input_pdf_path = "C:\Users\dell\Desktop\Tasks\CERTIFICATE _NAVEEN.pdf.pdf"
output_pdf_path = "C:\Users\dell\Desktop\Tasks\output.pdf"
old_text = "20JR1A05A3"
new_text = "20jr1a05a3"
replace_text_in_pdf(input_pdf_path, output_pdf_path, old_text, new_text)
