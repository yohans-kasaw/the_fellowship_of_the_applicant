import subprocess
import pyperclip
from time import sleep
import tempfile
import os

def wait_for_user_confirmation(step_description):
    """Pauses execution until the user enters 'c' to continue."""
    print(f"{step_description}\nPress Enter Key to continue.")
    input()

def copy_to_clipboard(text):
    """Copies text to the system clipboard."""
    pyperclip.copy(text)
    print("text has been copied to clipboard.")

def read_from_clipboard():
    """Reads text from the system clipboard."""
    return pyperclip.paste()

def open_editor_with_text(text, editor='neovide'):
    """Opens the text in a specified editor using a temporary file."""
    with tempfile.NamedTemporaryFile(delete=False, mode='w+', suffix='.txt') as tmpfile:
        tmpfile.write(text)
        tmpfile.flush()
        subprocess.run([editor, '+ZenMode', tmpfile.name])
        os.unlink(tmpfile.name)

def generate_research_prompt(job_description):
    """Generates a research prompt from a job description."""
    return f"""
Please conduct a thorough research on the company's culture, values, and more. Use multiple sources to get a comprehensive view. Here is the job description to guide your research:

{job_description}

Note: Browse at least 10 different sources for a well-rounded perspective.
"""

def generate_cover_letter_prompt(job_description, research_summary):
    """Generates a prompt for crafting a cover letter based on the research summary."""
    return f"""
Based on research on company and the job description, craft a cover letter that reflects the company's values and showcases qualifications. Start with a strong opening, include insights relevant to the position, and conclude with a compelling closing statement.

# Job Description
{job_description}

# Research Summary
{research_summary}
"""

def main():
    print("Step 1 ---------")
    wait_for_user_confirmation("Copy the job description and")
    
    job_description = read_from_clipboard()
    research_prompt = generate_research_prompt(job_description)
    copy_to_clipboard(research_prompt)

    print("Step 2 ---------")
    wait_for_user_confirmation("Review the copied research prompt at https://chatgpt.com/ and")
    
    company_research = read_from_clipboard()
    cover_letter_prompt = generate_cover_letter_prompt(job_description, company_research)
    copy_to_clipboard(cover_letter_prompt)

    print("Last Step ---------")
    wait_for_user_confirmation("Copy the final cover letter and")
    
    cover_letter = read_from_clipboard()
    open_editor_with_text(cover_letter)

    print("All steps completed. Your cover letter is ready for review in the editor.")

if __name__ == "__main__":
    main()
