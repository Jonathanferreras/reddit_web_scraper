import requests
from bs4 import BeautifulSoup

class RedditWebParser:
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36' }
    cookies = { 'over18' : '1' }

    def __init__(self, url):
        self.url = url
        html_data = requests.get(self.url, headers = RedditWebParser.headers, cookies = RedditWebParser.cookies)
        self.soup = BeautifulSoup(html_data.content, 'html.parser')

    def getHTML(self):
        return self.soup.prettify("utf-8")

    def getPost(self):
        post_div = self.soup.find('div', class_ = 'sitetable')
        post_content = post_div.find('div', class_ = 'md')

        return post_content

    def getComments(self):
        comment_div = self.soup.find('div', class_ = 'commentarea')
        comment_sitetable = comment_div.find('div', class_ = 'sitetable')
        comment_thing = comment_sitetable.findAll('div', class_ = 'thing')

        return comment_thing
