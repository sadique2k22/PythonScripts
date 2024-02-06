import os
import PyPDF2

def remove_last_page(pdf_file_path):
    # Open the PDF file
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        # Iterate through pages except the last one
        for page_num in range(len(reader.pages) - 1):
            writer.add_page(reader.pages[page_num])

        # Write the modified PDF to a new file
        with open(f"{os.path.splitext(pdf_file_path)[0]}_without_last_page.pdf", 'wb') as output_file:
            writer.write(output_file)

# Replace 'path_to_your_pdf_folder' with the path to the folder containing your PDF files
pdf_folder_path = 'files/'

# Iterate through each PDF file in the folder
for file_name in os.listdir(pdf_folder_path):
    if file_name.endswith('.pdf'):
        file_path = os.path.join(pdf_folder_path, file_name)
        remove_last_page(file_path)

print("Last pages removed from all PDF files in the folder.")