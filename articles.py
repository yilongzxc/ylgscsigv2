import requests
from bs4 import BeautifulSoup

class Sci:
    def __init__(self, link, cls):
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
                    url = heading.attrs['href']
                    titles.append(title + '''
''' + url + '''

''')
                    i += 1
        return titles

JAMA_Surgery = Sci("https://jamanetwork.com/journals/jamasurgery/currentissue", "article--title")
Journal_of_Vascular_Surgery = Sci("https://www.journals.elsevier.com/journal-of-vascular-surgery/recent-articles", "pod-listing-header")
World_Neurosurgery = Sci("https://www.journals.elsevier.com/world-neurosurgery-x/recent-articles", "pod-listing-header")
Clinical_Orthopedics_and_Trauma = Sci("https://www.journals.elsevier.com/journal-of-clinical-orthopaedics-and-trauma/recent-articles", "pod-listing-header")
Transplantation_Reviews = Sci("https://www.journals.elsevier.com/transplantation-reviews/recent-articles", "pod-listing-header")
Transplantation_Reports = Sci("https://www.journals.elsevier.com/transplantation-reports/recent-articles", "pod-listing-header")
Transplant_Immunology = Sci("https://www.journals.elsevier.com/transplant-immunology/recent-articles", "pod-listing-header")

# cd Desktop\python\python proj\yl sci
# ylsci-env\Scripts\activate.bat
