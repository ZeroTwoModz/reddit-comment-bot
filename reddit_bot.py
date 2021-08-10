import praw
import time
import json
from os import system, name
text = '''

  ▒███████▒▓█████  ██▀███   ▒█████    ██████ ▓█████  ███▄    █   ██████ ▓█████ 
  ▒ ▒ ▒ ▄▀░▓█   ▀ ▓██ ▒ ██▒▒██▒  ██▒▒██    ▒ ▓█   ▀  ██ ▀█   █ ▒██    ▒ ▓█   ▀ 
  ░ ▒ ▄▀▒░ ▒███   ▓██ ░▄█ ▒▒██░  ██▒░ ▓██▄   ▒███   ▓██  ▀█ ██▒░ ▓██▄   ▒███   
    ▄▀▒   ░▒▓█  ▄ ▒██▀▀█▄  ▒██   ██░  ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒  ▒   ██▒▒▓█  ▄ 
  ▒███████▒░▒████▒░██▓ ▒██▒░ ████▓▒░▒██████▒▒░▒████▒▒██░   ▓██░▒██████▒▒░▒████▒
  ░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░
  ░░▒ ▒ ░ ▒ ░ ░  ░  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░░ ░▒  ░ ░ ░ ░  ░
  ░ ░ ░ ░ ░   ░     ░░   ░ ░ ░ ░ ▒  ░  ░  ░     ░      ░   ░ ░ ░  ░  ░     ░   
    ░ ░       ░  ░   ░         ░ ░        ░     ░  ░         ░       ░     ░  ░
  ░  
                                                                          
'''
with open('config.json') as gg:
 config = json.load(gg)
def asd():
	r = praw.Reddit(username = config["username"],
				password = config["password"],
				client_id = config["client_id"],
				client_secret = config["client_secret"],
				user_agent = "idk lol")
	return r
    
def comment(r):
    for comment in r.subreddit('random').comments():
      system('cls' if name == 'nt' else 'clear')
      print(text)
      comment.reply(config["reply_text"])
      print(f" Comment ID: {comment.id}")
      print(f" Comment author: {comment.author}")
      time.sleep(60) 
r = asd()
while True:
	comment(r)