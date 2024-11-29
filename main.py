import subprocess
import sys

def run_script(script_name, *args):
    """Run a Python script with the given arguments."""
    command = [sys.executable, script_name] + list(args)
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error running {script_name}: {result.stderr}")
        sys.exit(1)
    else:
        print(f"{script_name} completed successfully: {result.stdout}")

def main():
    # Define the paths to your scripts and any arguments they need
    json_template_script = "json-template.py"
    html_pdf_script = "html-pdf.py"

    # Example arguments (adjust as needed)
    json_input = "path/to/your/input.json"
    html_template = "path/to/your/template.html"
    html_output = "path/to/your/output.html"
    pdf_output = "path/to/your/output.pdf"

    # Run the Json-template.py script
    run_script(json_template_script, json_input, html_template, html_output)

    # Run the html-pdf.py script
    run_script(html_pdf_script, html_output, pdf_output)

if __name__ == "__main__":
    main()
