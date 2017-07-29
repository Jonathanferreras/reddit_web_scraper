from RedditWebParser import RedditWebParser
import codecs
import os
import os.path
import re

class Submission(RedditWebParser):

    def __init__(self, url):
        self.url = url
        self.submission = RedditWebParser(self.url)
        self.title = self.submission.getTitle()
        self.title = re.sub('[''#%&{}\<>*?/$!:@""]', '', self.title)

    def writePost(self, output):
        post = self.submission.getPost()

        output.write('\n' + 'Post:' + '\n')
        for line in post:
            try:
                output.write(line.text)
            except AttributeError:
                continue
        output.write('\n')

    def writeComment(self, output):
        comments = self.submission.getComments()

        output.write('\n' + 'Comments:' + '\n')
        for comment in comments:
            try:
                output.write(comment.text)
            except AttributeError:
                print('Problem reading comment!')
                continue
        output.write('\n')

    def writeSubmission(self, new_path):
        submission_path = os.path.join(new_path, self.title + '.txt')

        with codecs.open(submission_path, "w", "utf-8-sig") as output:
            print('----------------------')
            print(f'extracting from: { self.url }')
            print('----------------------')

            output.write('\n' + f'SUBMISSION : { self.url }')
            self.writePost(output)
            self.writeComment(output)
        output.close()
