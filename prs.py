from bs4 import BeautifulSoup
import requests
import imgkit
URL = 'https://phdpu.edu.ua/course/oo-11pm-e-12pm-f-13pm-pv/'
page = requests.get(URL)
  # load the page content
text = page.content
  
soup = BeautifulSoup(text, "html.parser")
with open('output.html', "w", encoding = 'utf-8') as file:
    
    # prettify the soup object and convert it into a string
    file.write(str(soup.table.prettify()))

css = 'style.css'

imgkit.from_file('output.html','out.jpg', css=css)
