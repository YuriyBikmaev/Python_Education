import json
from bs4 import BeautifulSoup

datafile = open('Python_Education\Parser\webinars.json', 'r', encoding='utf-8')
data = json.load(datafile)
#[webinar["speaker"] for webinar in data]
#print([webinar["speaker"] for webinar in data])
datafile.close


htmlfile= open('Python_Education\Parser\skillbox.html', 'r', encoding='utf-8')
code = htmlfile.read()
soup = BeautifulSoup(code, "html.parser")
links = soup.findAll('a')
print(*[link.string for link in links])
