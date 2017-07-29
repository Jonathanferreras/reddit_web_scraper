import config
import os
import os.path
import praw
from Submission import Submission

reddit = praw.Reddit(user_agent = config.user_agent,
                     client_id = config.client_id,
                     client_secret = config.client_secret)

#specifing subreddit
subreddit = reddit.subreddit(config.subreddit)
subreddit2 = reddit.subreddit('all')
# #read names from text file and store in list
target_list = open('target_list.txt', 'r')
target_names = []

for name in target_list:
    target_names.append(name.rstrip())
    print('--------------------------------------')
    print(f'extracting { name } from target list...')
    print('--------------------------------------')
target_list.close()

author_submissions_urls = []
general_submissions_urls = []

for name in target_names:
    root_dir = os.getcwd()
    sub_dir = os.path.join(root_dir, 'target_data')
    name_dir = os.path.join(sub_dir, name)
    author_submissions = os.path.join(name_dir, 'author_submissions')
    general_submissions = os.path.join(name_dir, 'general_submissions')

    #creates folder for target if it does not exisit
    if not os.path.exists(author_submissions):
        os.makedirs(author_submissions)

    if not os.path.exists(general_submissions):
        os.makedirs(general_submissions)

    print(f'username: { name }')
    #storing author submissions urls into author submissons folder
    for author_data in subreddit.search('author:' + name):
        if 'reddit' in author_data.url:
            author_submissions_urls.append(author_data.url)
            print('------------------')
            print('extracting author submissions urls...')
            print('------------------')
            print(f'{ author_data.url }')

    for url in author_submissions_urls:
        author_submission = Submission(url)
        author_submission.writeSubmission(author_submissions)
    author_submissions_urls = []

    #storing general submissions_urls into general submissions folder
    for general_data in subreddit2.search('selftext:'+name):
        if 'reddit' in general_data.url:
            general_submissions_urls.append(general_data.url)
            print('------------------')
            print('extracting general submissions urls...')
            print('------------------')
            print(f'{ general_data.url }')

    for url in general_submissions_urls:
        general_submission = Submission(url)
        general_submission.writeSubmission(general_submissions)
    general_submissions_urls = []
