# PDF Duplicate Checker

This Python script helps you find and categorize duplicate PDF files within a specified directory.

## Features

- Calculates MD5 hash values of PDF files to identify duplicates.
- Writes the list of duplicate files to a text file, categorized by their hash values.

## Prerequisites

- Python 3.x

## Usage

1. Clone the repository or download the files to your local machine.

2. Install the required packages:


## Instructions

1. Open the `main.py` file.

2. Set the `pdf_directory` variable to the path of the directory where your PDF files are located.

3. Set the `output_file` variable to the desired path for the output file that will contain the list of duplicate files.

4. Save the changes.

5. Run the script:
    
        ```bash
        python main.py
        ```
        
6. The script will generate the output file with the duplicate PDF file paths, categorized by their hash values.

7. Open the output file to view the list of duplicate files.

## Customization

- You can modify the `calculate_hash` function in the `pdf_duplicates.py` file to use a different hashing algorithm if desired.

- Feel free to adjust the code to fit your specific needs or add additional functionalities.

## Notes

- Processing a large number of PDF files or files with large sizes may take significant time and resources. Consider running the script on a powerful machine or optimize the code as needed.

- Ensure that you have sufficient disk space for the output file, especially if you have a large number of duplicates.

## License

This project is licensed under the [MIT License](LICENSE).


