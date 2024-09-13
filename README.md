**AI-Powered Resume Parsing System**

**Overview**

This project is an AI-driven resume parsing tool that leverages Natural Language Processing (NLP) and Optical Character Recognition (OCR) to extract key information from resumes. The system uses a custom-trained spaCy Named Entity Recognition (NER) model to identify personal names, technologies, and client details from resumes in .docx format. Additionally, it processes embedded images within resumes using Tesseract OCR and outputs the results in a well-structured Excel format.

This tool is designed to streamline and automate resume parsing for recruiters, making the process faster, more efficient, and accurate.

**Features**

AI-Driven Parsing: Utilizes a custom-trained spaCy NER model to extract relevant information.

OCR Support: Scans and extracts text from embedded images within resumes using Tesseract OCR.

Technology Extraction: Searches for specific SAS-related technologies mentioned in the resume.

Client Identification: Extracts client names from resume text and tables.

Structured Output: Outputs the parsed information (Name, Technology, Client Names) into an Excel sheet.

Automated Resume Processing: Processes all .docx resumes in a given directory and creates a summary in a user-friendly Excel file.

**Getting Started**
    **Prerequisites**
Ensure you have the following software and libraries installed:

Python 3.x
spaCy
pytesseract
docx
pandas
openpyxl
Pillow

You can install the required Python libraries using:

pip install spacy pytesseract python-docx pandas openpyxl Pillow

**Setting Up Tesseract**

Install Tesseract OCR from here.
After installation, configure the Tesseract path in your environment if needed.

spaCy Model Setup:
You need a custom-trained NER model using spaCy. To train or load your model:

import spacy
nlp_custom = spacy.load("path_to_your_custom_model")

**Usage**

Input Directory: Place all .docx resume files in the input directory specified in the code.
Running the Script:
       - Update the input_directory and output_file paths in the script.
       - Run the script to process resumes:

python resume_parser.py

Output: The parsed information will be saved in an Excel file at the specified output path, with fields like Name, Technology, Client Names, and File Name.

Example:

input_directory = '/path/to/resume/folder/'
output_file = '/path/to/output_resumes.xlsx'

**Key Functions**

extract_name(file_name, text):
Extracts the candidate’s name using the filename and document content. It uses the custom NER model for better accuracy.
search_technology(text):
Identifies relevant technologies (e.g., SAS, SAS VIYA) from the resume text.
extract_client_names(doc, technology):
Extracts client names from tables and text, filtering out unwanted terms.
extract_text_from_images(docx_path):
Extracts text from embedded images in .docx resumes using Tesseract OCR.
process_resumes(input_directory, output_file):
Processes all resumes in a given directory and outputs structured data into an Excel sheet.

**Sample Output**

The output is an Excel file with the following columns:

Name: The candidate's name.
Technology: Detected technologies from the resume (e.g., SAS, Python).
Client Names: Client names extracted from the resume.
File Name: The original filename of the resume.
Contributions

Feel free to submit pull requests if you want to contribute to enhancing the functionality of this resume parsing tool. Suggestions and improvements are always welcome!

Credits

Author: Malaya Kumar Swain

License

This project is licensed under the MIT License - see the LICENSE file for details.

Future Enhancements

Expand support for more resume formats (e.g., PDF).
Add more customizable NER models for different industries.
Enhance technology extraction to support a wider range of keywords.
