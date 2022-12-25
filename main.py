import praw
import wget
import shutil
import os
from instabot import Bot
import glob
from dotenv import load_dotenv
load_dotenv()

print(os.getenv('INSTAUSER'),os.getenv('PASSWORD'))
cookie_del = glob.glob("config/*cookie.json")
if(cookie_del):
    os.remove(cookie_del[0])

bot = Bot()
bot.login(username=os.getenv('INSTAUSER'),
          password=os.getenv('PASSWORD'))

reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent="Python Program",
)

for submission in reddit.subreddit("rickandmorty").hot(limit=5):
    url = submission.url
    if(url.endswith(".jpg")):
        title = submission.title + ".jpg"
        caption = submission.title +'''.
    .
    .
    .
    .
    .
    .
    #rickandmortyvideos #rickandmortypop #rickandmortyfun #rickandmortydotcom #rickandmortynotofficial #rickandmortytime #rickandmortyamv #rickandmortyclips #rickandmortyeditsad #rickandmortyfunny #rickandmortyseason3 #rickandmortymeme #rickandmortyquotes #rickandmortycomic #rickandmortycosplay #rickandmortyseason4 #rickandmortyforever #rickandmortyfandom #rickandmortyfanart
    #adultswim'''
        filename = wget.download(url)
        print(filename)
        shutil.move(filename,"./posts/"+filename)
        bot.upload_photo("./posts/"+filename, caption=caption)
        break