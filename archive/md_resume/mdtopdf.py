import markdown
from weasyprint import HTML

with open('./resume_official.md', 'r', encoding='utf-8') as file:
    markdown_text = file.read()

html_text = markdown.markdown(markdown_text)

with open('./resume.css', 'r', encoding='utf-8') as file:
    css_text = file.read()
styled_html = f"<style>{css_text}</style>{html_text}"

HTML(string=styled_html).write_pdf('output.pdf')
