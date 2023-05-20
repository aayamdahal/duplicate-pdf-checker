from pdf_duplicates import find_duplicate_pdfs, write_duplicates_to_file

# Provide the path to the directory containing the PDF files
pdf_directory = "/home/aayam/check-pdf-duplicate/pdf"

# Find duplicate PDF files
duplicate_files = find_duplicate_pdfs(pdf_directory)

# Specify the output file path
output_file = "/home/aayam/check-pdf-duplicate/output.txt"

# Write duplicate PDF file paths to the output file
write_duplicates_to_file(duplicate_files, output_file)

print("Duplicates written to the file successfully.")
