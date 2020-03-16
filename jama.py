import requests
from bs4 import BeautifulSoup

def section():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}
    result = requests.get("https://jamanetwork.com/journals/jamasurgery/currentissue", headers = headers)
    content = result.content

    soup = BeautifulSoup(content, 'html.parser')
    articles = soup.find_all(class_="article--title")

    titles = []

    for article in articles:
        if article.find_parent(class_="issue-group group--in-this-issue-of-jama-surgery") is not None or article.find_parent(class_="issue-group group--viewpoint") is not None or article.find_parent(class_="issue-group group--original-investigation") is not None:
            heading = article.find('a')
            if heading is not None:
                title = heading.get_text()
                url = heading.attrs['href']
                titles.append(title + '''
''' + url + '''

''')
    return titles
