import praw
import urllib.request
import urllib.error
import os.path
import time
from threading import Thread
import random


reddit = praw.Reddit(client_id='XXX',
                     client_secret='XXX',
                     user_agent='app for downloading pics from subreddits',
                     username='XXX',
                     password='XXX')

urls = []
titles = []

sub = reddit.subreddit('subbredit')
for post in sub.top(limit=300):
    urls.append(post.url)
    titles.append(post.title)

p = os.getcwd() + '\directory'
if not os.path.exists(p):
    os.makedirs(p)
    os.chdir(p)
else:
    os.chdir(p)


def replace(word):
    chars = '"?/|*:<>'
    for c in chars:
        word = word.replace(c, '')
    return word


correct_titles = list(map(replace, titles))


def download(thread_name, names, url, begin):
    c = 1
    error = 0
    for i in range(begin, len(url), 4):
        n = names[i] + ".jpg"
        if os.path.isfile(n):
            n = n[:-4] + str(random.randint(0, 100)) + n[-4:]
        try:
            urllib.request.urlretrieve(url[i], str(n))
        except urllib.error.URLError:
            error = error + 1
            print(thread_name + " Error occured")
            continue
        print(thread_name + ": " + str(c))
        c = c + 1
    print("Thread" + thread_name + " ended " + 'with ' + str(error) + " errors occured")


def threads():
    start = time.time()
    t1 = Thread(target=download, args=("Thread 1", correct_titles, urls, 0))
    t2 = Thread(target=download, args=("Thread 2", correct_titles, urls, 1))
    t3 = Thread(target=download, args=("Thread 3", correct_titles, urls, 2))
    t4 = Thread(target=download, args=("Thread 4", correct_titles, urls, 3))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    finish = time.time()
    print("It took " + str(finish - start) + ' seconds to download')


threads()


