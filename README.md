# Resume Generation Toolkit

## Overview
This toolkit automates the process of generating professional resumes in HTML & PDF formats (HTML & PDF) from a JSON source.

## Prerequisites

### Software Requirements
- Python 3.8+
- wkhtmltopdf (PDF conversion)

### Installation

1. Clone the repository

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Install wkhtmltopdf
- Windows: Download from [wkhtmltopdf official site](https://wkhtmltopdf.org/downloads.html)
- macOS: `brew install wkhtmltopdf`
- Linux: `sudo apt-get install wkhtmltopdf`

## Project Structure
- `main.py`: Orchestrates the entire resume generation process
- `json-template.py`: Converts JSON to HTML
- `html-pdf.py`: Converts HTML to PDF and DOCX
- `template.html`: Jinja2 HTML template for resume rendering
- `requirements.txt`: Project dependency list
- `template_resume.json`: JSON resume template

## Usage

### Creating a Resume
1. Copy `template_resume.json`
2. Fill in your personal and professional details or use LLM to complete
3. Save as `[your_name]_resume.json`

### Generate Resumes
```bash
python main.py
```

## Customization
- Modify `template.html` to change resume layout
- Adjust `json-template.py` for different rendering options

## Troubleshooting
- Ensure all dependencies are installed
- Check file paths in scripts
- Verify wkhtmltopdf installation

## Contributing
Contributions are welcome! Please submit pull requests or open issues.

