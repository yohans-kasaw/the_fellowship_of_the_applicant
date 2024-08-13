from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Create a Firefox Options object
options = Options()
options.profile = "/home/yohansh/.mozilla/firefox/68maxacf.joforces"


# Setup WebDriver with the specified options
driver = webdriver.Firefox(options=options)

# Open a webpage
driver.get('https://chatgpt.com/?model=gpt-4')
# Find the input field using its name or ID and fill it
input_field = driver.find_element('id', 'prompt-textarea')
input_field.send_keys('Hello am yohans, from python code')
#
# # Optionally, submit the form
input_field.submit()
#
# # Close the browser
# driver.close()
