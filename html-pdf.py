import pdfkit
import os

def html_to_pdf(html_file, output_pdf, margins=None):
    try:
        # Ensure the HTML file exists
        if not os.path.isfile(html_file):
            raise FileNotFoundError(f"The HTML file {html_file} does not exist.")

        # Default margins if not provided
        if margins is None:
            margins = {
                'top': '16mm',
                'right': '18mm',
                'bottom': '21mm',
                'left': '18mm'
            }

        # Configure PDF options with margins
        options = {
            'margin-top': margins['top'],
            'margin-right': margins['right'],
            'margin-bottom': margins['bottom'],
            'margin-left': margins['left']
        }

        # Convert HTML to PDF
        pdfkit.from_file(html_file, output_pdf, options=options, configuration=pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'))
        print(f"PDF created successfully: {output_pdf}")
        return output_pdf

    except Exception as e:
        print(f"An error occurred converting {html_file} to PDF: {str(e)}")
        return None

def convert_all_html_to_pdf(margins=None):
    # Find all HTML resume files
    html_files = [f for f in os.listdir('.') if f.endswith('_rendered_resume.html')]
    
    # If no HTML files found, raise an error
    if not html_files:
        raise FileNotFoundError("No *_rendered_resume.html files found in the current directory")
    
    # Store converted PDF filenames
    converted_pdfs = []
    
    # Convert each HTML file to PDF
    for html_file in html_files:
        # Generate output PDF filename
        output_pdf = html_file.replace('_rendered_resume.html', '_resume.pdf')
        
        try:
            converted_pdf = html_to_pdf(html_file, output_pdf, margins)
            if converted_pdf:
                converted_pdfs.append(converted_pdf)
        except Exception as e:
            print(f"Error converting {html_file} to PDF: {e}")
    
    return converted_pdfs

# This allows the script to be imported without automatically running
if __name__ == "__main__":
    convert_all_html_to_pdf()