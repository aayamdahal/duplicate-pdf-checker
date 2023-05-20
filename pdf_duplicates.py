import os
import hashlib

def calculate_hash(file):
    hasher = hashlib.md5()
    with open(file, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def find_duplicate_pdfs(directory):
    duplicates = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                hash_value = calculate_hash(file_path)
                if hash_value in duplicates:
                    duplicates[hash_value].append(file_path)
                else:
                    duplicates[hash_value] = [file_path]
    
    return duplicates

def write_duplicates_to_file(duplicates, output_file):
    with open(output_file, 'w') as f:
        for hash_value, file_paths in duplicates.items():
            if len(file_paths) > 1:
                f.write(f"Duplicate PDFs (Hash: {hash_value}):\n")
                for file_path in file_paths:
                    f.write(f"- {file_path}\n")
                f.write("\n")
