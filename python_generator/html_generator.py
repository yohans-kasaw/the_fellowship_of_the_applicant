import json
import subprocess

def generate_header(all_data):
    return """
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yohans Hailu Kasaw Portfolio</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
    <main class="bg-white dark:bg-gray-950 text-gray-900 dark:text-gray-50 font-sans">
        <div class="px-4 py-8 md:px-4 md:py-8 container mx-auto">
"""

def generate_contact_info_section(all_data, section_style, border_style):
    return f"""
    <section class="{section_style} {border_style}">
        <h1 class="text-2xl font-bold">{all_data['address']['name']}</h1>
        <div class="text-gray-500 dark:text-gray-400 mt-2 space-x-4">
            <span>📞 {all_data['address']['phone']}</span>
            <span>✉️ <a href="mailto:{all_data['address']['email']}" class="text-blue-500 hover:text-blue-600 dark:text-blue-400 dark:hover:text-blue-500">{all_data['address']['email']}</a></span>
            <span>📍 {all_data['address']['location']}</span>
            <span>🔗 <a href="{all_data['address']['linkedin']}" class="text-blue-500 hover:text-blue-600 dark:text-blue-400 dark:hover:text-blue-500">LinkedIn</a></span>
            <span>🔗 <a href="{all_data['address']['github']}" class="text-blue-500 hover:text-blue-600 dark:text-blue-400 dark:hover:text-blue-500">GitHub</a></span>
        </div>
        <p class="pt-4 text-gray-700 dark:text-gray-400">
            {all_data['summary']}
        </p>
    </section>
"""

def generate_section(all_data, section_style, border_style, key):
    section = all_data[key]
    border = f" {border_style}" if key != "achievements" else ""
    html = f'<section class="{section_style}{border}">'
    html += f"<h2 class='text-xl font-bold mb-2'>{key.capitalize()}</h2>"
    html += "<div class='space-y-2'>"
    for item in section['items']:
        details = "<ul class='list-disc pl-4 text-gray-700 dark:text-gray-400'>" + "".join(f"<li>{detail}</li>" for detail in item.get('details', [])) + "</ul>"
        html += f"""
                        <div>
                            <h3 class="font-semibold">{item.get('institution', item.get('role', ''))}</h3>
                            <p class="text-gray-500 dark:text-gray-400">{item.get('period', '')}</p>
                            {details}
                        </div>
        """
    html += "</div></section>"
    return html

def generate_html(all_data):
    section_style = "pb-2 pt-2"
    border_style = "border-b border-gray-200 dark:border-gray-800"
    
    html_content = generate_header(all_data)
    html_content += generate_contact_info_section(all_data, section_style, border_style)
    
    sections = ['education', 'experience', 'projects', 'skills', 'achievements']
    for key in sections:
        html_content += generate_section(all_data, section_style, border_style, key)
    
    html_content += """
        </div>
    </main>
</body>
</html>
    """
    return html_content


if __name__ == "__main__":
    # open the json file in nevim, let it save the file. and then continue

    json_resume_name = "floey"
    json_file = open(f"/home/yohansh/JobSearch/json_resumes/{json_resume_name}.json", "r")
    all_data = json.loads(json_file.read())

    file_name = json_file.name.split("/")[-1].replace("json", "html")
    file_path = f"/home/yohansh/JobSearch/generated_resume/{file_name}"

    file = open(file_path, "w")
    file.write(generate_html(all_data))

    file.close()
    subprocess.run(["google-chrome-stable", file_path])

    print("HTML generated successfully!")
