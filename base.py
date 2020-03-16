import requests
from bs4 import BeautifulSoup

class Sci:
    def __init__(self, base_link, link, cls):
        self.base_link = base_link
        self.link = link
        self.cls = cls

    def site(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}
        result = requests.get(self.link, headers = headers)
        content = result.content

        soup = BeautifulSoup(content, 'html.parser')
        articles = soup.find_all(class_=self.cls)

        titles = []
        i = 0
        for article in articles:
            if i<=7:
                heading = article.find('a')
                if heading is not None:
                    title = heading.get_text()
                    url = self.base_link + heading.attrs['href']
                    titles.append(title + '''
''' + url + '''

''')
                    i += 1
        return titles


Journal_of_Neurology_Neurosurgery_and_Psychiatry = Sci("https://jnnp.bmj.com", "https://jnnp.bmj.com/content/early/recent", "highwire-cite highwire-cite-highwire-article highwire-citation-bmjj-pap clearfix")
Annals_of_Hepato_Pancreato_Biliary_Surgery = Sci("http://www.ahbps.org", "http://www.ahbps.org/journal/list.html?pn=lastest", "j_ti")
