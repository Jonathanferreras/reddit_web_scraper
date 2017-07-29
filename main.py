import codecs
import config
import os
import os.path
import praw
from RedditWebParser import RedditWebParser

reddit = praw.Reddit(user_agent = config.user_agent,
                     client_id = config.client_id,
                     client_secret = config.client_secret)

#specifing subreddit
subreddit = reddit.subreddit(config.subreddit)

# #read names from text file and store in list
target_list = open('target_list.txt', 'r')
target_names = []

for name in target_list:
    target_names.append(name.rstrip())
    print('--------------------------------------')
    print(f'extracting { name } from target list...')
    print('--------------------------------------')
target_list.close()


#extract data from web pages
urls = []
for name in target_names:
    print(f'username: { name }')
    for author_data in subreddit.search('author:' + name):
        if 'reddit' in author_data.url:
            urls.append(author_data.url)
            print('------------------')
            print('extracting urls...')
            print('------------------')
            print(f'{ author_data.url }')

    file_name = name + '.txt'
    root_dir = os.getcwd()
    sub_dir = os.path.join(root_dir, 'target_data')
    new_path = os.path.join(sub_dir, name)

    #creates folder for target if it does not exisit
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    post_comment_path = os.path.join(new_path, file_name)

    #write to text file contents from urls
    with codecs.open(post_comment_path, "w", "utf-8-sig") as output:
        counter = 1
        for url in urls:
            try:
                print('----------------------')
                print(f'extracting from: { url }')
                print('----------------------')

                #create instance of RWP class
                parser = RedditWebParser(url)
                html = parser.getComments()
                output.write(f'post { counter }: { url }')
                output.write('\n' + str(html) + '\n')

                counter = counter + 1
            except AttributeError:
                print('Oops no comment found!')
                continue
    output.close()
    urls = []
