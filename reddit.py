from typing import Type
from datetime import datetime
import praw
import time
import json
import requests

url = "https://www.reddit.com/r/Your Community Name/new.json?sort=new"
post = []
commented_post = []
comment = "Thank You For Posting. Hope You enjoy your time"

def fetch_recent(): 
    req = requests.get(url, headers={'User-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'})
    json_data = req.text
    parsed_json = (json.loads(json_data))
    distro = parsed_json['data']['children']
    for eachSubmission in distro:
        data = eachSubmission['data']['name']
        if data not in post:
            post.append(data)
    return

def submission_comment(post_id):
    reddit = praw.Reddit(
    client_id="Your client ID",
    client_secret="Your Seceret ID",
    password="Your Account Password",
    user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    username="Your Username",
)
    reddit.validate_on_submit = True
    commented_post.append(post_id)
    Submission = reddit.submission(id=post_id)
    # print(type(Submission.author.name))
    comment = "Thank You "+ Submission.author.name +" For Posting. Hope You enjoy your time"
    print("Commented on : "+ Submission.author.name+" Post")
    Submission.reply(comment)

def split_post():
    for single_post in post:
        single_post = single_post.split("_")
        post_id = single_post[1]
        if post_id not in commented_post:
            submission_comment(post_id)

while True:    
    fetch_recent()
    split_post()
    time.sleep(6)
    # print(commented_post)
    
