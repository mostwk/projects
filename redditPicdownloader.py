import praw
import urllib.request
import urllib.error
import os.path
import time
from threading import Thread

reddit = praw.Reddit(client_id='xxx',
                     client_secret='xxx',
                     user_agent='app for downloading pics from subreddits',
                     username='xxx',
                     password='xxx')

urls1 = []
urls2 = []
names1 = []
names2 = []
sub = reddit.subreddit('subreddit')
even = True
for post in sub.top(limit=300):
    if even is True:
        urls1.append(post.url)
        names1.append(post.title)
        even = False
    else:
        urls2.append(post.url)
        names2.append(post.title)
        even = True

p = os.getcwd() + '\goods1'
if not os.path.exists(p):
    os.makedirs(p)
    os.chdir(p)
else:
    os.chdir(p)


def repl(word):
    chars = '"?/|*:<>'

    for c in chars:
        word = word.replace(c, '')
    return word


last1 = list(map(repl, names1))
last2 = list(map(repl, names2))

dic1 = dict(zip(urls1, last1))
dic2 = dict(zip(urls2, last2))


def download(name, url):
    c = 1
    error = 0
    for pic in url:
        n = url[pic] + ".jpg"
        try:
            urllib.request.urlretrieve(pic, str(n))
        except urllib.error.URLError:
            error = error + 1
            print(name + " Error occured")
            continue
        print(name + " :" + str(c))
        c = c + 1
    print("Thread" + name + " ended " + 'with ' + str(error) + " errors occured")


def threads():
    start = time.time()
    t1 = Thread(target=download, args=("Thread 1", dic1))
    t2 = Thread(target=download, args=("Thread 2", dic2))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    finish = time.time()
    print("it took " + str(finish - start) + ' seconds to download')


threads()

