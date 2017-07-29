import requests
import codecs
from bs4 import BeautifulSoup

class RedditWebParser:
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36' }
    cookies = { 'over18' : '1' }
    # values = { 'limit' : '' }

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
        # comment_entry = comment_thing.find('div', class_ = 'entry')
        # comment_usertext = comment_entry.find('form', class_ = 'usertext')
        # comment_usertext_body = comment_usertext.find('div', class_ = 'usertext-body')
        # comments = comment_thing.find('p')

        return comment_thing


# url = 'https://www.reddit.com/r/DarkNetMarkets/comments/6ogj7g/hansa_and_alphabay_busted_megathread/'
#
# test = RedditWebParser(url)
#
# # html = test.getPost()
# html = test.getComments()
#
# with codecs.open("test_output", "w", "utf-8-sig") as temp:
#     temp.write(str(html))
