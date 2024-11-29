from jinja2 import Environment, FileSystemLoader
import json
import os

def convert_resume(json_filename):
    """
    Convert a single JSON resume to HTML and DOCX.
    """
    # Load JSON data
    with open(json_filename, 'r') as file:
        resume_data = json.load(file)

    # Setup Jinja2 environment and load the HTML template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    # Render the template with the JSON data
    rendered_html = template.render(resume_data)

    # Save the rendered HTML to a file (optional, for debugging purposes)
    filename_base = resume_data["contact_info"]["name"].replace(" ", "_").lower()
    with open(f'{filename_base}_rendered_resume.html', 'w') as html_file:
        html_file.write(rendered_html)
   
def convert_all_resumes():
    # Find all JSON resume files
    json_files = [f for f in os.listdir('.') if f.endswith('_resume.json')]
    
    # If no JSON files found, raise an error
    if not json_files:
        raise FileNotFoundError("No *_resume.json files found in the current directory")
    
    # Store converted filenames
    converted_files = []
    
    # Convert each JSON resume
    for json_file in json_files:
        try:
            converted_file = convert_resume(json_file)
            converted_files.append(converted_file)
            print(f"Converted {json_file} to {converted_file}")
        except Exception as e:
            print(f"Error converting {json_file}: {e}")
    
    return converted_files

# This allows the script to be imported without automatically running
if __name__ == "__main__":
    convert_all_resumes()